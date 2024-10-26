import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('seu caminho.csv', usecols=lambda column: column != 'Data')
df['Fechamento ajustado**'] = df['Fechamento ajustado**'].str.replace(',', '.').astype(float)
df['Volume'] = df['Volume'].str.replace('.', '').astype(float)

media_aritmetica_gerdau = df['Fechamento ajustado**'].mean()
media_geometrica_gerdau = np.prod(df['Fechamento ajustado**']) ** (1 / len(df['Fechamento ajustado**']))
media_ponderada_gerdau = np.average(df['Fechamento ajustado**'], weights=df['Volume'])
cv_fechamento_ajustado_gerdau = (df['Fechamento ajustado**'].std() / df['Fechamento ajustado**'].mean()) * 100
variancia_fechamento_ajustado_gerdau = df['Fechamento ajustado**'].var()
desvio_padrao_fechamento_ajustado_gerdau = df['Fechamento ajustado**'].std()
coef_correlacao_gerdau = df['Fechamento ajustado**'].corr(df['Volume'])
df['Z-score'] = (df['Fechamento ajustado**'] - df['Fechamento ajustado**'].mean()) / df['Fechamento ajustado**'].std()


media_aritmetica_gerdau = round(media_aritmetica_gerdau, 3)
media_geometrica_gerdau = round(media_geometrica_gerdau, 3)
media_ponderada_gerdau = round(media_ponderada_gerdau, 3)
cv_fechamento_ajustado_gerdau = round(cv_fechamento_ajustado_gerdau, 3)
variancia_fechamento_ajustado_gerdau = round(variancia_fechamento_ajustado_gerdau, 3)
desvio_padrao_fechamento_ajustado_gerdau = round(desvio_padrao_fechamento_ajustado_gerdau, 3)
coef_correlacao_gerdau = round(coef_correlacao_gerdau, 3)
df['Z-score'] = df['Z-score'].round(3)

covariancia_fechamento_volume = df[['Fechamento ajustado**', 'Volume']].cov().iloc[0, 1]
covariancia_fechamento_volume = round(covariancia_fechamento_volume, 3)

print("Estatísticas para 'Fechamento ajustado**' da empresa GERDAU:\n")
print("Média Aritmética:", media_aritmetica_gerdau)
print("Média Geométrica:", media_geometrica_gerdau)
print("Média Ponderada:", media_ponderada_gerdau)
print("\nCoeficiente de Variação (%):", cv_fechamento_ajustado_gerdau)
print("Coeficiente de Correlação:", coef_correlacao_gerdau)
print("Variância:", variancia_fechamento_ajustado_gerdau)
print("Desvio Padrão:", desvio_padrao_fechamento_ajustado_gerdau)
print("Covariância entre 'Fechamento ajustado**' e 'Volume':", covariancia_fechamento_volume)
print("\n")
print(df[['Fechamento ajustado**', 'Z-score']])
print("\n\n============================================================\n\n")

df2 = pd.read_csv('seu caminho.csv', usecols=lambda column: column != 'Data')
df2['Fechamento ajustado**'] = df2['Fechamento ajustado**'].str.replace(',', '.').astype(float)
df2['Volume'] = df2['Volume'].str.replace('.', '').astype(float)

media_aritmetica_eletrobras = df2['Fechamento ajustado**'].mean()
media_geometrica_eletrobras = np.prod(df2['Fechamento ajustado**']) ** (1 / len(df2['Fechamento ajustado**']))
media_ponderada_eletrobras = np.average(df2['Fechamento ajustado**'], weights=df2['Volume'])
cv_fechamento_ajustado_eletrobras = (df2['Fechamento ajustado**'].std() / df2['Fechamento ajustado**'].mean()) * 100
variancia_fechamento_ajustado_eletrobras = df2['Fechamento ajustado**'].var()
desvio_padrao_fechamento_ajustado_eletrobras = df2['Fechamento ajustado**'].std()
coef_correlacao_eletrobras = df2['Fechamento ajustado**'].corr(df2['Volume'])
df2['Z-score'] = (df2['Fechamento ajustado**'] - df2['Fechamento ajustado**'].mean()) / df2['Fechamento ajustado**'].std()


media_aritmetica_eletrobras = round(media_aritmetica_eletrobras, 3)
media_geometrica_eletrobras = round(media_geometrica_eletrobras, 3)
media_ponderada_eletrobras = round(media_ponderada_eletrobras, 3)
cv_fechamento_ajustado_eletrobras = round(cv_fechamento_ajustado_eletrobras, 3)
variancia_fechamento_ajustado_eletrobras = round(variancia_fechamento_ajustado_eletrobras, 3)
desvio_padrao_fechamento_ajustado_eletrobras = round(desvio_padrao_fechamento_ajustado_eletrobras, 3)
coef_correlacao_eletrobras = round(coef_correlacao_eletrobras, 3)
df2['Z-score'] = df2['Z-score'].round(3)

covariancia_fechamento_volume = df2[['Fechamento ajustado**', 'Volume']].cov().iloc[0, 1]
covariancia_fechamento_volume = round(covariancia_fechamento_volume, 3)

print("Estatísticas para 'Fechamento ajustado**' da empresa ELETROBRAS:\n")
print("Média Aritmética:", media_aritmetica_eletrobras)
print("Média Geométrica:", media_geometrica_eletrobras)
print("Média Ponderada:", media_ponderada_eletrobras)
print("\nCoeficiente de Variação (%):", cv_fechamento_ajustado_eletrobras)
print("Coeficiente de Correlação:", coef_correlacao_eletrobras)
print("Variância:", variancia_fechamento_ajustado_eletrobras)
print("Desvio Padrão:", desvio_padrao_fechamento_ajustado_eletrobras)
print("Covariância entre 'Fechamento ajustado**' e 'Volume':", covariancia_fechamento_volume)
print("\n")
print(df2[['Fechamento ajustado**', 'Z-score']])


