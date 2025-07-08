import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    print(f"Loading data from Yahoo Finance for: {ticker}")
    try:
        data = yf.download(ticker, period=period)
        if data.empty:
            print("❌ No data found.")
            return pd.DataFrame()
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"❌ Failed to fetch data: {e}")
        return pd.DataFrame()
