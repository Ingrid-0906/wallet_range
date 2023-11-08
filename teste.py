import pandas as pd

df = pd.read_csv('PA-16990.csv', delimiter='|')

df_pivot = df.pivot_table(index='data_posicao', columns='categoria', values='valor_total', aggfunc='sum', fill_value=None).ffill()
df_pl = df.groupby(['data_posicao'])['pl_total_mes_atual'].max().to_frame().iloc[-1]

lista_weight = {'categoria': df_pivot.columns, 'weight':[]}
for x in df_pivot.iloc[-1]:
    v = x / df_pl.iloc[-1]
    lista_weight['weight'].append(v)
    
lw = pd.DataFrame(data=lista_weight)
# Removed Custodia Remunerada / Proventos / Saldo Projetado
lw = lw.drop(index=[3, 9, 11], axis=1).reset_index()
df_pivot = df_pivot.drop(columns=['Custodia Remunerada','Proventos','Saldo Projetado']).reset_index()

# Verify if this is 1.0
#print(round(lw.sum().iloc[1], 1))

print(lw['weight'])