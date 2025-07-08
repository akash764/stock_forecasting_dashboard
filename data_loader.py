import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    try:
        data = yf.download(ticker, period=period)
        if data.empty:
            print(f"[Warning] Empty data returned for: {ticker}")
            return None
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"[Error] Failed to fetch data for {ticker}: {e}")
        return None
