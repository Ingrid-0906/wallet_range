import numpy as np
import math
import streamlit as st
from plotly import graph_objs as go

class Tools:

    def gen_graph_3d(tx, p_vol, p_ret, e_r, mat_cov):
        rf = ((tx + 1) ** (1 / 252)) - 1
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter3d(
            x=list(p_vol*100),
            y=list(p_ret*100),
            z=list(((p_ret - rf) / p_vol)*100),
            name='Carteiras',
            mode='markers',
            marker=dict(size=6)
        ))

        fig.add_trace(go.Scatter3d(
            x=list(p_vol[:3]*100),
            y=list(p_ret[:3]*100),
            z=list(((p_ret[:3] - rf) / p_vol[:3])*100),
            name='Top Carteira',
            mode='markers',
            marker=dict(size=10, color='yellow')
        ))

        # tight layout
        fig.update_layout(scene=dict(xaxis_title='Risco',
                                    yaxis_title='Retorno',
                                    zaxis_title='índice Sharpe'),
                        margin=dict(l=0, r=0, b=0))
        fig.update_traces(hovertemplate='Risco=%{x}<br>Retorno=%{y}<br>Sharpe=%{z}<extra></extra>', 
                        selector=dict(type='scatter3d'))
        return st.plotly_chart(fig, use_container_width=True) 
