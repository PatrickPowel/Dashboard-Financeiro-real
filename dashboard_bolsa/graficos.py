import plotly.express as px

def grafico_preco(df):
    fig = px.line(
        df,
        x=df.index,
        y="Close",
        title="Preço da Ação"
    )

    fig.show()