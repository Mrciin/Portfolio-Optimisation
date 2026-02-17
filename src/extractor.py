from src.settings import TICKERS,START_DATE,END_DATE
import yfinance as yf
import pandas as pd

def extract_data(tickers=TICKERS,start_date=START_DATE,end_date=END_DATE):

    stock_data={}
    for ticker in tickers:
        df=yf.download(ticker,start=start_date,end=end_date,progress=False)
        if df.empty:
            print(f"No data found for {ticker}")
            continue
        stock_data[ticker]=df
        print (stock_data[ticker])
    return stock_data


