import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    try:
        data = yf.download(ticker, period=period)
        if data.empty:
            print("⚠️ No data found for this symbol.")
            return None
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"⚠️ Failed to fetch stock data: {e}")
        return None
