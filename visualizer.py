import plotly.graph_objects as go
import streamlit as st

def plot_forecast(data, forecast):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"], mode='lines', name='Forecast'))

    fig.update_layout(title="📈 Stock Price Forecast (Prophet)",
                      xaxis_title="Date", yaxis_title="Price",
                      legend=dict(x=0, y=1), height=500)

    st.plotly_chart(fig, use_container_width=True)
