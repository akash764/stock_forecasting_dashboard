import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    try:
        print(f"Loading data for: {ticker}")
        data = yf.download(ticker, period=period, proxy="https://query1.finance.yahoo.com")
        if data.empty:
            print("❌ No data found for ticker.")
        return data
    except Exception as e:
        print(f"❌ Error fetching data for {ticker}: {e}")
        return pd.DataFrame()
