import streamlit as st
import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="1y"):
    try:
        print(f"Loading data from Yahoo Finance for: {ticker}")
        data = yf.download(ticker, period=period)
        if data.empty:
            print("❌ No data found for ticker.")
            return pd.DataFrame()
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return pd.DataFrame()

