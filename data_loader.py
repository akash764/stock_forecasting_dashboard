import streamlit as st
import pandas as pd
import requests

API_KEY = "XJ6A5KT15AMKXTWN"

def load_stock_data(ticker, period="2y"):
    st.write(f"Loading data for: {ticker}")  # Optional for Streamlit display

    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={ticker}&outputsize=full&apikey={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if "Error Message" in data:
            st.error("❌ Invalid symbol or request: " + data["Error Message"])
            return pd.DataFrame()

        if "Note" in data:
            st.warning("⚠️ API limit reached. Please wait and try again.")
            return pd.DataFrame()

        if "Time Series (Daily)" not in data:
            st.error("❌ Unexpected response format.")
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

    except Exception as e:
        st.error(f"❌ Exception occurred: {e}")
        return pd.DataFrame()
