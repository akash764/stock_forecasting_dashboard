import pandas as pd
import requests

API_KEY = "your_alpha_vantage_api_key_here"

def load_stock_data(ticker, period="2y"):
    print(f"Loading data from Alpha Vantage for: {ticker}")
    
    # Daily time series data
    API_KEY = "XJ6A5KT15AMKXTWN"

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=full&apikey={API_KEY}"

    
    try:
        response = requests.get(url)
        data = response.json()

        if "Time Series (Daily)" not in data:
            print(" Invalid data format from API.")
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
        
        print(f" Downloaded {len(df)} rows from Alpha Vantage")
        return df

    except Exception as e:
        print(f" API error: {e}")
        return pd.DataFrame()
