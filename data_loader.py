import pandas_datareader.data as web
from datetime import datetime, timedelta

def load_stock_data(ticker, period="2y"):
    try:
        end = datetime.today()
        start = end - timedelta(days=730)  # 2 years
        df = web.DataReader(ticker, "av-alpha-vantage", start, end, api_key="IZB96UGQUMS5G0ZV")
        df.reset_index(inplace=True)
        df.rename(columns={"close": "Close", "date": "Date"}, inplace=True)
        return df
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None
