import streamlit as st
import pandas as pd

from data_loader import load_stock_data
from forecast_model import train_prophet_model, make_forecast
from visualizer import plot_forecast

st.set_page_config(page_title="Stock Forecasting (Prophet)", layout="wide")
st.title("Stock Market Forecasting Dashboard (Prophet)")

# Sidebar inputs
st.sidebar.header("Stock Settings")
ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, INFY.NS)", value="AAPL")
forecast_days = st.sidebar.slider("Forecast Days", 7, 90, 30)

if ticker:
    data = load_stock_data(ticker)

    if data is None or data.empty:
        st.error("Failed to fetch stock data. Please check the ticker symbol and try again.")
    else:
        st.subheader(f"Historical Data for {ticker}")
        st.line_chart(data.set_index("Date")["Close"])

        with st.spinner("Training Prophet model..."):
            model = train_prophet_model(data)
            forecast = make_forecast(model, forecast_days)

        st.subheader("Forecasted Prices")
        plot_forecast(data, forecast)

        # Show forecast table
        forecast_df = forecast[["ds", "yhat"]].tail(forecast_days)
        forecast_df.columns = ["Date", "Predicted Price"]
        st.dataframe(forecast_df)

        # Download button
        csv = forecast_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Forecast", data=csv, file_name=f"{ticker}_forecast.csv")
