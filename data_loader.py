import pandas as pd
import requests

API_KEY = "XJ6A5KT15AMKXTWN"

def load_stock_data(ticker, period="2y"):
    print(f"Loading data for: {ticker}")

    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={ticker}&outputsize=full&apikey={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        # Print raw response to debug
        print("API response:", data)

        # Error Handling
        if "Error Message" in data:
            print("❌ Invalid symbol or request:", data["Error Message"])
            return pd.DataFrame()

        if "Note" in data:
            print("⚠️ Rate limit hit:", data["Note"])
            return pd.DataFrame()

        if "Time Series (Daily)" not in data:
            print("❌ Unexpected response format.")
            return pd.DataFrame()

        # Parse DataFrame
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

        print(f"✅ Loaded {len(df)} rows.")
        return df

    except Exception as e:
        print("❌ Exception:", e)
        return pd.DataFrame()
