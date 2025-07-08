import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    try:
        print(f"Downloading stock data for: {ticker}")
        data = yf.download(ticker, period=period)

        if data.empty:
            print(f" No data returned for: {ticker}")
            return pd.DataFrame()

        data.reset_index(inplace=True)
        print(f" Downloaded {len(data)} rows for {ticker}")
        return data

    except Exception as e:
        print(f"❌ Exception while downloading data for {ticker}: {e}")
        return pd.DataFrame()
