import streamlit as st
import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    st.write(f"Loading data from Yahoo Finance for: {ticker}")
    
    try:
        data = yf.download(ticker, period=period)
        if data.empty:
            st.error("❌ Failed to fetch data. Please check the symbol or try again.")
            return pd.DataFrame()

        data.reset_index(inplace=True)
        return data

    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")
        return pd.DataFrame()
