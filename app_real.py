import streamlit as st
import pandas as pd
from plotly import graph_objs as go
from app_classe_real import *
from utils import tool

def range_boundary(title, min, max, show):
    min = round(min*100, 2)
    max = round(max*100, 2)
    
    if show:
        disabled = False
    else:
        disabled = True
    
    if min != max:
        slider = st.slider(title, 
                  min, 
                  max, 
                  min, 
                  disabled=disabled)
    else:
        slider = st.slider(title, 
                  0.1, 
                  max, 
                  0.1, 
                  disabled=disabled)
    return slider
     
if __name__ == "__main__":
    # Setting: Data Start Here...
    st.set_page_config(
        page_title = 'Wallet Alloc Asset v.3.0',
        page_icon = '✅',
        layout = 'wide'
    )
    
    lbl_1 = "Aluguel"
    lbl_2 = "Ações"
    lbl_3 = "COE"
    lbl_4 = "Derivativos de Balção"
    lbl_5 = "Fundos Imobiliarios"
    
    lbl_6 = "Fundos de Investimento"
    lbl_7 = "NPS"
    lbl_8 = "Previdencia Privada"
    lbl_9 = "Produtos Estruturados"
    lbl_10 = "Renda Fixa"
    
    lbl_11 = "Tesouro Direto"
    
    col1, col2 = st.columns([0.9, 0.1], gap='small')
    
    with col1:
        st.title('Wallet Alloc Asset v.3.0')
        st.subheader("Timeframe 6mo")
    with col2:
        st.markdown(f"<h6 style='color: white; padding: 0; margin: 0;'>Atual Posição</h6>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: red; padding: 0; margin: 0;'>{round(i_ret[0]*100, 2)}%</h1>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='color: gray; padding: 0; margin: 0;'>{round(i_vol[0]*100, 2)}% volátil</h5>", unsafe_allow_html=True)
    st.markdown(f"<br><br>", unsafe_allow_html=True)
    
    # ROW 1
    pos_1, pos_2, pos_3, pos_4, pos_5 = st.columns(5)
    with pos_1:
        pos_1 = st.metric(lbl_1, round(cart_position['position'].iloc[0]*100, 2), round(e_r[lbl_1]*100, 2))
    with pos_2:
        pos_2 = st.metric(lbl_2, round(cart_position['position'].iloc[1]*100, 2), round(e_r[lbl_2]*100, 2))
    with pos_3:
        pos_3 = st.metric(lbl_3, round(cart_position['position'].iloc[2]*100, 2), round(e_r[lbl_3]*100, 2))
    with pos_4:
        pos_4 = st.metric(lbl_4, round(cart_position['position'].iloc[3]*100, 2), round(e_r[lbl_4]*100, 2))
    with pos_5:
        pos_5 = st.metric(lbl_5, round(cart_position['position'].iloc[4]*100, 2), round(e_r[lbl_5]*100, 2))
        
    ticker_1, ticker_2, ticker_3, ticker_4, ticker_5 = st.columns(5)
    with ticker_1:
        able_1 = st.checkbox('abilitar', key='able_1')
        ticker_1 = range_boundary(title=lbl_1, min=lower_uper_bands['min'].iloc[0], max=lower_uper_bands['max'].iloc[0], show=able_1)
    with ticker_2:
        able_2 = st.checkbox('abilitar', key='able_2')
        ticker_2 = range_boundary(title=lbl_2, min=lower_uper_bands['min'].iloc[1], max=lower_uper_bands['max'].iloc[1], show=able_2)
    with ticker_3:
        able_3 = st.checkbox('abilitar', key='able_3')
        ticker_3 = range_boundary(title=lbl_3, min=lower_uper_bands['min'].iloc[2], max=lower_uper_bands['max'].iloc[2], show=able_3)
    with ticker_4:
        able_4 = st.checkbox('abilitar', key='able_4')
        ticker_4 = range_boundary(title=lbl_4, min=lower_uper_bands['min'].iloc[3], max=lower_uper_bands['max'].iloc[3], show=able_4)
    with ticker_5:
        able_5 = st.checkbox('abilitar', key='able_5')
        ticker_5 = range_boundary(title=lbl_5, min=lower_uper_bands['min'].iloc[4], max=lower_uper_bands['max'].iloc[4], show=able_5)
    
    # ROW 2    
    pos_6, pos_7, pos_8, pos_9, pos_10 = st.columns(5)
    with pos_6:
        pos_6 = st.metric(lbl_6, round(cart_position['position'].iloc[5]*100, 2), round(e_r[lbl_6]*100, 2))
    with pos_7:
        pos_7 = st.metric(lbl_7, round(cart_position['position'].iloc[6]*100, 2), round(e_r[lbl_7]*100, 2))
    with pos_8:
        pos_8 = st.metric(lbl_8, round(cart_position['position'].iloc[7]*100, 2),  round(e_r[lbl_8]*100, 2))
    with pos_9:
        pos_9 = st.metric(lbl_9, round(cart_position['position'].iloc[8]*100, 2), round(e_r[lbl_9]*100, 2))
    with pos_10:
        pos_10 = st.metric(lbl_10, round(cart_position['position'].iloc[9]*100, 2), round(e_r[lbl_10]*100, 2))
    
    ticker_6, ticker_7, ticker_8, ticker_9, ticker_10 = st.columns(5)
    with ticker_6:
        able_6 = st.checkbox('abilitar', key='able_6')
        ticker_6 = range_boundary(title=lbl_6, min=lower_uper_bands['min'].iloc[5], max=lower_uper_bands['max'].iloc[5], show=able_6)
    with ticker_7:
        able_7 = st.checkbox('abilitar', key='able_7')
        ticker_7 = range_boundary(title=lbl_7, min=lower_uper_bands['min'].iloc[6], max=lower_uper_bands['max'].iloc[6], show=able_7)
    with ticker_8:
        able_8 = st.checkbox('abilitar', key='able_8')
        ticker_8 = range_boundary(title=lbl_8, min=lower_uper_bands['min'].iloc[7], max=lower_uper_bands['max'].iloc[7], show=able_8)
    with ticker_9:
        able_9 = st.checkbox('abilitar', key='able_9')
        ticker_9 = range_boundary(title=lbl_9, min=lower_uper_bands['min'].iloc[8], max=lower_uper_bands['max'].iloc[8], show=able_9)
    with ticker_10:
        able_10 = st.checkbox('abilitar', key='able_10')
        ticker_10 = range_boundary(title=lbl_10, min=lower_uper_bands['min'].iloc[9], max=lower_uper_bands['max'].iloc[9], show=able_10)
    
    ticker_11, pos_11 = st.columns([0.2, 0.8])
    with ticker_11:
        pos_10 = st.metric(lbl_11, round(cart_position['position'].iloc[10]*100, 2), round(e_r[lbl_11]*100, 2))
        able_11 = st.checkbox('abilitar', key='able_11')
        ticker_11 = range_boundary(title=lbl_10, min=lower_uper_bands['min'].iloc[10], max=lower_uper_bands['max'].iloc[10], show=able_11)
    
    if able_1 or able_2 or able_3 or able_4 or able_5 or able_6 or able_7 or able_8 or able_9 or able_10 or able_11:
        st.session_state.disabled = False
        
        if able_1:
            r = ticker_1
            col = lbl_1
        if able_2:
            r = ticker_2
            col = lbl_2
        if able_3:
            r = ticker_3
            col = lbl_3
        if able_4:
            r = ticker_4
            col = lbl_4
        if able_5:
            r = ticker_5
            col = lbl_5
        if able_6:
            r = ticker_6
            col = lbl_6
        if able_7:
            r = ticker_7
            col = lbl_7
        if able_8:
            r = ticker_8
            col = lbl_8
        if able_9:
            r = ticker_9
            col = lbl_9
        if able_10:
            r = ticker_10
            col = lbl_10
        if able_11:
            r = ticker_11
            col = lbl_11
    else:
        r = 0
        col = ''
        st.session_state.disabled = True
        
    btn = st.button('Calcular', type='primary', key='btn', disabled=st.session_state.disabled)
    
    if btn:
        minRisk, MaxRet = st.tabs(['Menor Risco', 'Maior Retorno'])
        cenarios_df = cenarios_df
        data = cenarios_df[cenarios_df[col]<=r]
        dt_risk = data[data['retorno']>0].sort_values(by='volatil', ascending=True)[:10]
        dt_risk['retorno'] = round(dt_risk['retorno'], 2)
        dt_risk['volatil'] = round(dt_risk['volatil'], 2)
        
        dt_ret = data[data['retorno']>0].sort_values(by='retorno', ascending=False)[:10]
        dt_ret['retorno'] = round(dt_ret['retorno'], 2)
        dt_ret['volatil'] = round(dt_ret['volatil'], 2)
        
        with minRisk:
            if len(dt_risk) > 0:
                st.markdown("### Recomendados")
                c1, c2, c3 = st.columns(3)
                dt_chart = np.round(dt_risk.iloc[:,[2,3,4,5,6,7,8,9,10,11,12]])
                with c1:
                    st.markdown(f"<h5 style='color: white;'>#1 Carteira</h5>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='color: white;'>{round(dt_risk['retorno'].iloc[0], 5)}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h5 style='color: gray;'>{round(dt_risk['volatil'].iloc[0], 2)}% volátil</h5>", unsafe_allow_html=True)
                    st.bar_chart(dt_chart.iloc[0], color="#2727c2", use_container_width=True)

                with c2:
                    st.markdown(f"<h5 style='color: white;'>#2 Carteira</h5>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='color: white;'>{round(dt_risk['retorno'].iloc[1], 5)}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h5 style='color: gray;'>{round(dt_risk['volatil'].iloc[1], 2)}% volátil</h5>", unsafe_allow_html=True)
                    st.bar_chart(dt_chart.iloc[1], color="#ec4563", use_container_width=True)

                with c3:
                    st.markdown(f"<h5 style='color: white;'>#3 Carteira</h5>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='color: white;'>{round(dt_risk['retorno'].iloc[2], 5)}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h5 style='color: gray;'>{round(dt_risk['volatil'].iloc[2], 2)}% volátil</h5>", unsafe_allow_html=True)
                    st.bar_chart(dt_chart.iloc[2], color="#6ded66", use_container_width=True)
                
                row_1, row_2 = st.columns([0.4, 0.6])
                with row_1:
                    tool.Tools.gen_graph_3d(tx, dt_risk['volatil'], dt_risk['retorno'], e_r, mat_cov)
                with row_2:
                    st.markdown("### Outras Opções")
                    st.dataframe(data=dt_risk.iloc[2:], use_container_width=True, hide_index=True)
            else:
                st.write('Não há cenários com retornos positivos para essa carteira no momento.')
                st.write(data)
        with MaxRet:
            if len(dt_ret) > 0:
                st.markdown("### Recomendados")
                c1, c2, c3 = st.columns(3)
                dt_chart = np.round(dt_risk.iloc[:,[2,3,4,5,6,7,8,9,10,11,12]])
                with c1:
                    st.markdown(f"<h5 style='color: white;'>#1 Carteira</h5>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='color: white;'>{round(dt_ret['retorno'].iloc[0], 5)}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h5 style='color: gray;'>{round(dt_ret['volatil'].iloc[0], 2)}% volátil</h5>", unsafe_allow_html=True)
                    st.bar_chart(dt_chart.iloc[0], color="#2727c2", use_container_width=True)

                with c2:
                    st.markdown(f"<h5 style='color: white;'>#2 Carteira</h5>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='color: white;'>{round(dt_ret['retorno'].iloc[1], 5)}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h5 style='color: gray;'>{round(dt_ret['volatil'].iloc[1], 2)}% volátil</h5>", unsafe_allow_html=True)
                    st.bar_chart(dt_chart.iloc[1], color="#ec4563", use_container_width=True)

                with c3:
                    st.markdown(f"<h5 style='color: white;'>#3 Carteira</h5>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='color: white;'>{round(dt_ret['retorno'].iloc[2], 5)}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h5 style='color: gray;'>{round(dt_ret['volatil'].iloc[2], 2)}% volátil</h5>", unsafe_allow_html=True)
                    st.bar_chart(dt_chart.iloc[2], color="#6ded66", use_container_width=True)
                
                row_1, row_2 = st.columns([0.4, 0.6])
                with row_1:
                    tool.Tools.gen_graph_3d(tx, dt_ret['volatil'], dt_ret['retorno'], e_r, mat_cov)
                with row_2:
                    st.markdown("### Outras Opções")
                    st.dataframe(data=dt_ret.iloc[2:], use_container_width=True, hide_index=True)
            else:
                st.write('Não há cenários com retornos positivos para essa carteira no momento.')
                st.write(data)
                