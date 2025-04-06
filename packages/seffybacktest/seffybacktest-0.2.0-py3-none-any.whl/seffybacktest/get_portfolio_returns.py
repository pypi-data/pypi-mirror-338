from seffybacktest.get_price_data import get_price_data
import yfinance as yf
import numpy as np
import pandas as pd

def get_portfolio_returns(tickers, weights, start_date, end_date):
    if len(tickers) != len(weights):
        raise ValueError("Tickers and weights must be the same length")

    weights = np.array(weights, dtype=np.float64)
    if not np.isclose(weights.sum(), 1.0):
        weights /= weights.sum()

    # Download data
    data = get_price_data(
        tickers,
        start=start_date,
        end=end_date,
        threads=False,
        group_by='ticker',
        auto_adjust=False
    )

    # Extract adjusted close prices across tickers
    try:
        price_data = data.xs('Adj Close', level='Price', axis=1)
    except KeyError:
        try:
            price_data = data.xs('Close', level='Price', axis=1)
        except KeyError:
            raise ValueError("Neither 'Adj Close' nor 'Close' found in the data.")

    price_data = price_data.dropna()

    # Calculate daily returns
    returns = price_data.pct_change().dropna()

    # Compute portfolio returns
    if len(tickers) == 1:
        portfolio_returns = returns.squeeze()
    else:
        portfolio_returns = returns @ weights

    portfolio_returns.index = portfolio_returns.index.tz_localize(None)
    return portfolio_returns

if __name__ == "__main__":
    tickers = ['AAPL', 'NVDA']
    weights = [0.45, 0.55]
    start_date = '2021-01-01'
    end_date = '2025-03-20'

    returns = get_portfolio_returns(tickers, weights, start_date, end_date)
    print(returns.head())
