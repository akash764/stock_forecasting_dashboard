def load_stock_data(ticker, period="2y"):
    print(f"Loading data from Alpha Vantage for: {ticker}")
    API_KEY = "XJ6A5KT15AMKXTWN"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=full&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        
        # Print full response for debugging
        print(data)

        if "Time Series (Daily)" not in data:
            st.error("⚠️ Error from API: " + data.get("Note", "Unknown error."))
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
        
        return df

    except Exception as e:
        st.error(f"API error: {e}")
        return pd.DataFrame()
