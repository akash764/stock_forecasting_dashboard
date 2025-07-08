import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def prepare_data(data, window_size=60):
    """
    Prepares sequences of stock prices for training the LSTM model.
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

    x, y = [], []
    for i in range(window_size, len(scaled_data)):
        x.append(scaled_data[i - window_size:i, 0])
        y.append(scaled_data[i, 0])

    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))

    return x, y, scaler

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def forecast_prices(model, recent_data, scaler, days=7):
    """
    Forecast future prices using trained model.
    """
    predictions = []
    current_input = recent_data.copy()

    for _ in range(days):
        input_reshaped = np.reshape(current_input, (1, current_input.shape[0], 1))
        pred = model.predict(input_reshaped, verbose=0)
        predictions.append(pred[0, 0])

        # append predicted value and remove oldest
        current_input = np.append(current_input[1:], pred[0, 0])

    predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    return predicted_prices.flatten()
