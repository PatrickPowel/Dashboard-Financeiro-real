import streamlit as st
import plotly.graph_objects as go
from dados import baixar_dados
from indicadores import retorno, volatilidade

st.set_page_config(page_title="Bolsa Brasileira", layout="wide")

st.title("📈 Dashboard Financeiro Premium")

ativo = st.selectbox("Escolha o Ativo", ["PETR4", "VALE3", "ITUB4"])

df = baixar_dados(ativo)

# Médias móveis
df["MM20"] = df["Close"].rolling(20).mean()
df["MM50"] = df["Close"].rolling(50).mean()

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Retorno %", round(retorno(df),2))
col2.metric("Volatilidade %", round(volatilidade(df),2))
col3.metric("Preço Atual", round(df["Close"].iloc[-1],2))
col4.metric("Máxima", round(df["High"].max(),2))

# Candlestick
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=df.index,
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"],
    name="Preço"
))

fig.add_trace(go.Scatter(
    x=df.index,
    y=df["MM20"],
    name="MM20"
))

fig.add_trace(go.Scatter(
    x=df.index,
    y=df["MM50"],
    name="MM50"
))

fig.update_layout(height=700)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Últimos dados")
st.dataframe(df.tail())