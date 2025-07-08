import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    try:
        data = yf.download(ticker, period=period)
        if data.empty:
            raise ValueError("yfinance returned empty data")
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"❌ Error fetching stock data for {ticker}: {e}")
        return pd.DataFrame()  # return empty df to trigger Streamlit error
