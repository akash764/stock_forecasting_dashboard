from prophet import Prophet
import pandas as pd

def train_prophet_model(data):
    df = pd.DataFrame()
    df["ds"] = data["Date"]
    df["y"] = data["Close"]

    model = Prophet(daily_seasonality=True)
    model.fit(df)
    return model

def make_forecast(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
