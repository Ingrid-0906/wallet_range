import numpy as np
import pandas as pd
from source import gen_base
from bonds import max_sharpe, min_risk

def filter_cenarios(r, col, cenarios):
    if r != '':
        alloc_asset = cenarios[cenarios[col]>r].sort_values(by='retorno', ascending=False)[:3]
        return alloc_asset*100
    else:
        alloc_asset = cenarios.sort_values(by='retorno', ascending=False)[:3]
        return alloc_asset*100 


if __name__ == "__main__":
    frame = '3mo'
    tickers = ["ITSA4.SA","VIVT3.SA","SBSP3.SA","PETR4.SA","VALE3.SA"]
    # indicator = ["BOVA11.SA"] # FOR ASSETS STUDY IS NECESSARY A BENCHMARK
    weight = [0.15, 0.25, 0.20, 0.25, 0.15] #This will be modified by range group
    
    # COLLECCTING DATA
    precos = gen_base.GenerateBase.get_yf_data(tickers=tickers, frame=frame)
    _, _, e_r, _, mat_cov = gen_base.GenerateBase.calculate_stats(precos)
    
    # BUILDING THE SCENARIOS
    n_ativos = len(tickers)
    p_ret, p_vol, p_pesos = gen_base.GenerateBase.generate_portfolios(n_ativos=n_ativos, e_r=e_r, mat_cov=mat_cov)
    # CREATING THE DATAFRAME OF ALL SCENARIOS
    pesos_df = pd.DataFrame(data=p_pesos, columns=tickers)
    rv_df = pd.DataFrame(data={'retorno': p_ret, 'volatil': p_vol}, columns=['retorno', 'volatil'])
    cenarios_df = pd.concat([rv_df, pesos_df], axis=1, join='inner')
    
    # GENERATING THE ACTUAL WALLET POSITION
    i_ret, i_vol = gen_base.GenerateBase.generate_position(pesos=weight, e_r=e_r, mat_cov=mat_cov)
    
    # GENERATING THE UPPER AND LOWER BANDS
    min_loc = 0.01
    tx = 0.09
    
    band_1 = max_sharpe.MaxSharpe(min_loc, tx, e_r, mat_cov, n_ativos)
    band_2 = min_risk.MinRisk(min_loc, e_r, mat_cov, n_ativos)
    
    pos_carteira = {
        'peso_otimo': np.array(weight), 
        'return_otimo': np.array(i_ret), 
        'volatil_otimo': np.array(i_vol)
        }
    
    # CREATE THE LOWER & UPPER BANDS + POSITION
    cart_band_1 = pd.DataFrame(data=band_1['peso_otimo'], index=tickers, columns=['max_sharpe'])
    cart_band_2 = pd.DataFrame(data=band_2['peso_otimo'], index=tickers, columns=['min_risk'])
    cart_position = pd.DataFrame(data=pos_carteira['peso_otimo'], index=tickers, columns=['position'])
    # MERGING ALL
    lower_uper_bands = pd.concat([cart_band_1, cart_band_2], axis=1, join='inner')
    
    # FILTERING TO SHOW THE BEST 3 ALLOCATIONS
    col = 'ITSA4.SA'
    r = '' # Peso determinado pelo usuário
    alloc = filter_cenarios(r=r, col=col, cenarios=cenarios_df)
    
    
    