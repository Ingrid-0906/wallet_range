import pandas as pd
import numpy as np
import yfinance as yf

class GenerateBase:
    def get_yf_data(tickers, frame):
        """
        
            Faz o download da fonte de dados do preço de fechamento junto ao yahoo finance.
            
            pars:
             - tickers: nome dos ativos
            
            vars:
             - precos: Dataframe com todos os tickers e seus respectivos valores de fechamento passados
             - tickers: lista com nome de ativos para buscar preços
                
            return:
             - precos
        """
        
        precos = pd.DataFrame()
        novo_nome = []
                
        for ticker in tickers:
            try:
                ticker = yf.Ticker(ticker)
                precos[ticker] = ticker.history(period=frame, interval='1d')["Close"]
            except Exception as e:
                print(f"Erro ao processar o ativo {ticker}: {e}")
                continue
            
        for i in range(len(tickers)):
            elemento = str(tickers[i][:tickers[i].find('.SA')])
            novo_nome.append(elemento)

        precos.columns = novo_nome
        return precos


    def calculate_stats(precos):
        """
            Calcula oo retorno, volatilidade, risco e covariancia entre os ativo(s)
             
            pars:
            - precos: dataframe com todo o historico de precos da carteira
             
            vars:
            - retornos: retorno atual
            - rotulo: nome dos ativos
            - e_r: media dos retornos
            - vol: volatilidade dos retornos
            - mat_cov: matriz de covariancia dos ativos
             
            return:
            - retornos, rotulo, e_r, vol, mat_cov
        """
        
        retornos = precos.pct_change().dropna()
        rotulo= retornos.columns.to_list()
        e_r=retornos.mean()
        vol=retornos.std()
        mat_cov=retornos.cov()
        return retornos, rotulo, e_r, vol, mat_cov
  

    def generate_portfolios(n_ativos, e_r, mat_cov):
        """
            Simulation that generates n_portifolios accordingly their individual but collective return and risk.
            
            vars:
             - p_ret: total return of a portfolio
             - p_vol: total volatility of a portfolio
             - p_pesos: individual weight of each stock
            
            return:
             - p_ret, p_vol, p_pesos
        """
        
        p_ret = []
        p_vol = []
        p_pesos = []

        for _ in range(3000):
            pesos = np.random.random(n_ativos)
            pesos = pesos / np.sum(pesos)
            p_pesos.append(pesos)

            returns = np.dot(pesos, e_r)
            p_ret.append(returns)

            var = mat_cov.mul(pesos, axis=0).mul(pesos, axis=1).sum().sum()
            dp = np.sqrt(var)
            p_vol.append(dp)

        p_ret = np.array(p_ret)
        p_vol = np.array(p_vol)
        p_pesos = np.array(p_pesos)

        return p_ret, p_vol, p_pesos


    def generate_position(pesos, e_r, mat_cov):
        """
            Generate the inicial position or a fictional pposition for each class.
            
            return:
             - p_ret, p_vol
        """
        
        p_ret = []
        p_vol = []

        returns = np.dot(pesos, e_r)
        p_ret.append(returns)

        var = mat_cov.mul(pesos, axis=0).mul(pesos, axis=1).sum().sum()
        dp = np.sqrt(var)
        p_vol.append(dp)
        return p_ret, p_vol
