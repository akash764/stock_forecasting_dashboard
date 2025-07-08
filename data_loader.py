# data_loader.py
import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    try:
        data = yf.download(ticker, period=period)
        if data.empty:
            return None
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
