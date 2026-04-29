import numpy as np

def retorno(df):
    preco_inicial = df["Close"].iloc[0]
    preco_final = df["Close"].iloc[-1]
    return (preco_final / preco_inicial - 1) * 100

def volatilidade(df):
    retornos = df["Close"].pct_change().dropna()
    return retornos.std() * (252 ** 0.5) * 100