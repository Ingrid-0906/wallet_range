import numpy as np
import pandas as pd
from source import gen_base
from bonds import max_sharpe, min_risk


# 1. COLLECCTING DATA
precos = pd.read_csv('base_BBC.csv', delimiter=';', decimal=',', index_col=['Data'])
tickers = precos.columns
weight = [0.65, 0.10, 0.12, 0.08, 0.05] # This will be modified by range group
min_loc = 0.01
tx = 1.0

# TRANSFORMING THE WEIGHT INTO A SINGLE UNIT OF PRICE: NORMALIZATION
new_precos = pd.DataFrame()
for x in range(len(tickers)):
    new_precos[precos.columns[x]] = precos[precos.columns[x]]/weight[x]


# 2. CALCULATING THE RETURN AND COVARIANCE
_, _, e_r, vol, mat_cov = gen_base.GenerateBase.calculate_stats(new_precos)

# 3. BUILDING THE SCENARIOS
p_ret, p_vol, p_pesos = gen_base.GenerateBase.generate_portfolios(n_ativos=len(tickers), e_r=e_r, mat_cov=mat_cov)

# 3.1. CREATING THE DATAFRAME OF ALL SCENARIOS
pesos_df = pd.DataFrame(data=p_pesos, columns=tickers)
rv_df = pd.DataFrame(data={'retorno': p_ret, 'volatil': p_vol}, columns=['retorno', 'volatil'])
cenarios_df = pd.concat([rv_df, pesos_df], axis=1, join='inner')

# 4. GENERATING THE ACTUAL WALLET POSITION // RISK AND RETORN
i_ret, i_vol = gen_base.GenerateBase.generate_position(pesos=weight, e_r=e_r, mat_cov=mat_cov)

# 5. GENERATING THE UPPER AND LOWER BANDS
band_1 = max_sharpe.MaxSharpe(min_loc, tx, e_r, mat_cov, len(tickers))
band_2 = min_risk.MinRisk(min_loc, e_r, mat_cov, len(tickers))

pos_carteira = {
    'peso': np.array(weight), 
    'retorn': np.array(i_ret), 
    'volatil': np.array(i_vol)
    }

# 5.1. CREATE THE LOWER & UPPER BANDS + POSITION
cart_band_1 = pd.DataFrame(data=band_1['peso_otimo'], index=tickers, columns=['max_sharpe'])
cart_band_2 = pd.DataFrame(data=band_2['peso_otimo'], index=tickers, columns=['min_risk'])
cart_position = pd.DataFrame(data=pos_carteira['peso'], index=tickers, columns=['position'])

# 5.2. MERGING ALL BANDS
lower_uper_bands = pd.concat([cart_band_1, cart_band_2], axis=1, join='inner')
lower_uper_bands['min'] = lower_uper_bands.min(axis=1)
lower_uper_bands['max'] = lower_uper_bands.max(axis=1)
