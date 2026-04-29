import streamlit as st
from dados import baixar_dados
from indicadores import retorno, volatilidade

st.title("Dashboard Bolsa Brasileira")

ativo = st.selectbox("Escolha Ativo", ["PETR4", "VALE3", "ITUB4"])

df = baixar_dados(ativo)

st.write(df.tail())

st.metric("Retorno %", round(retorno(df),2))
st.metric("Volatilidade %", round(volatilidade(df),2))