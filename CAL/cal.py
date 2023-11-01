import numpy as np
import math
import scipy.optimize as sco

def CAL(a, tx, max_sharpe_X, e_r, mat_cov):

    rf = ((tx + 1)**(1/252))-1 #Calcular taxa livre de risco
    
    def port_vol(pesos): #Função de cálculo de risco
        return math.sqrt(np.dot(pesos,np.dot(mat_cov, pesos)))
    
    def port_ret(pesos): #Função de cálculo de retorno
        return np.sum(e_r*pesos)
    
    wp = (port_ret(max_sharpe_X)-rf)/(a*port_vol(max_sharpe_X)**2)
    return wp