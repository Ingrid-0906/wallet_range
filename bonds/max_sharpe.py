import numpy as np
import math
from scipy.optimize import minimize

def MaxSharpe(min_loc, tx, e_r, mat_cov, n_ativos):
    """
        Calculate de max sharpe, that can be used as an upper or lower bond.
        
        parameters:
        -...
        
        vars:
        -...
    """
    
    rf = ((tx + 1)**(1/252))-1 #Calcular taxa livre de risco
    
    def port_vol(pesos): #Função de cálculo de risco
        return math.sqrt(np.dot(pesos,np.dot(mat_cov, pesos)))
    
    def port_ret(pesos): #Função de cálculo de retorno
        return np.sum(e_r*pesos)
    
    # Estimar carteira de Sharpe Ratio máximo
    def min_func_sharpe(pesos):
        return -(port_ret(pesos)-rf)/port_vol(pesos)
    
    tpl2 = 1 - min_loc
    restri = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
    bnds = tuple((min_loc, tpl2) for _ in range(n_ativos))
    pesos_i = np.array(n_ativos * [1 / n_ativos])

    # Otimização do Sharpe
    otim_sharpe = minimize(min_func_sharpe, pesos_i, method='SLSQP', bounds=bnds, constraints=restri)
    peso_otimo = otim_sharpe['x']
    ret_otimo = port_ret(otim_sharpe['x'])
    vol_otimo = port_vol(otim_sharpe['x'])
    return {
        'peso_otimo': peso_otimo,
        'returno_otimo': ret_otimo,
        'volatil_otimo': vol_otimo
    }