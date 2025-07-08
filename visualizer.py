import plotly.graph_objects as go
import streamlit as st
import pandas as pd

def plot_forecast(data, forecast, window_size=60):
    """
    Plots actual historical stock prices and forecasted future prices.
    """
    last_date = data["Date"].iloc[-1]
    forecast_dates = pd.date_range(last_date, periods=len(forecast) + 1, closed="right")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=forecast_dates, y=forecast, mode='lines+markers', name='Forecast'))

    fig.update_layout(title="Stock Price Forecast",
                      xaxis_title="Date", yaxis_title="Price",
                      legend=dict(x=0, y=1), height=500)

    st.plotly_chart(fig, use_container_width=True)
