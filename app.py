import streamlit as st
import pandas as pd

from data_loader import load_stock_data
from forecast_model import prepare_data, build_model, forecast_prices
from visualizer import plot_forecast

st.set_page_config(page_title="📈 Stock Forecasting Dashboard", layout="wide")
st.title("📈 Stock Market Forecasting Dashboard")

# Sidebar
st.sidebar.header("Enter Stock Details")
ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, INFY.NS)", value="AAPL")
forecast_days = st.sidebar.slider("Days to Forecast", 3, 30, 7)

if ticker:
    # Load data
    st.subheader(f"📊 Historical Data for {ticker}")
    data = load_stock_data(ticker)
    
    if data.empty:
        st.error("⚠️ Failed to load stock data. Please check the ticker.")
    else:
        st.write(data.tail())
        st.line_chart(data.set_index("Date")["Close"])

        # Prepare data for LSTM
        with st.spinner("⏳ Preparing data and training model..."):
            x, y, scaler = prepare_data(data)
            model = build_model((x.shape[1], 1))
            model.fit(x, y, epochs=5, batch_size=32, verbose=0)

            # Forecast
            last_sequence = x[-1].flatten()
            forecast = forecast_prices(model, last_sequence, scaler, days=forecast_days)

        # Show forecast chart
        st.subheader("🔮 Forecasted Prices")
        plot_forecast(data, forecast)

        # Show forecast table
        forecast_dates = pd.date_range(data["Date"].iloc[-1], periods=forecast_days+1, closed="right")
        forecast_df = pd.DataFrame({"Date": forecast_dates, "Predicted Price": forecast})
        st.dataframe(forecast_df)

        # Optional: Download forecast
        csv = forecast_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Forecast as CSV", data=csv, file_name=f"{ticker}_forecast.csv", mime="text/csv")
