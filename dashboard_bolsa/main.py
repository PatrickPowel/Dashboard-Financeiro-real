from dados import baixar_dados
from indicadores import retorno, volatilidade
from graficos import grafico_preco

df = baixar_dados("PETR4")

print("Retorno:", round(retorno(df),2), "%")
print("Volatilidade:", round(volatilidade(df),2), "%")

grafico_preco(df)

print(df.head())