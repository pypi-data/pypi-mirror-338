import yfinance as yf
import pandas as pd

def get_price_data(tickers, start=None, end=None, **kwargs):
    data = yf.download(tickers, start=start, end=end, **kwargs)
    if isinstance(data.columns, pd.MultiIndex):
        if 'Adj Close' in data.columns.levels[0]:
            return data['Adj Close']
        elif 'Close' in data.columns.levels[0]:
            return data['Close']
    else:
        if 'Adj Close' in data:
            return data['Adj Close']
        elif 'Close' in data:
            return data['Close']
    raise ValueError("Neither 'Adj Close' nor 'Close' price data available.")
