import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="2y"):
    data = yf.download(ticker, period=period)
    data.reset_index(inplace=True)
    return data
