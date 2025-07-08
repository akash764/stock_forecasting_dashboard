import pandas as pd
import requests

API_KEY = "XJ6A5KT15AMKXTWN"

def load_stock_data(ticker, period="2y"):
    print(f"Loading data for ticker: {ticker}")
    
    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={ticker}&outputsize=full&apikey={API_KEY}"
    )

    try:
        response = requests.get(url)
        print("API raw response:", response.text[:500])  # Only print first 500 chars

        data = response.json()

        if "Time Series (Daily)" not in data:
            print("❌ API Error or Invalid Ticker:", data.get("Note") or data.get("Error Message") or "Unknown issue")
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
        
        print(f"✅ Downloaded {len(df)} rows for {ticker}")
        return df

    except Exception as e:
        print(f"❌ API error: {e}")
        return pd.DataFrame()
