import yfinance as yf
import pandas as pd

def baixar_dados(ativo, periodo="1y"):
    ticker = ativo + ".SA"
    df = yf.download(ticker, period=periodo)

    # Remove multiindex se existir
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df