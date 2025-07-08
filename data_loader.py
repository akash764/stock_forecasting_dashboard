import streamlit as st
import requests
import pandas as pd

def load_stock_data(ticker):
    API_KEY = st.secrets["ALPHA_VANTAGE_API_KEY"]
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=compact&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        print("❌ Unexpected API response:", data)
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. adjusted close": "Adj Close",
        "6. volume": "Volume"
    })
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.astype(float).reset_index().rename(columns={"index": "Date"})

    return df
