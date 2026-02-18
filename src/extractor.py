from src.settings import TICKERS,START_DATE,END_DATE
import yfinance as yf
import pandas as pd


#
def process_a_single_ticker(ticker_df: pd.DataFrame) -> pd.DataFrame:
    ticker_df= ticker_df[["Close"]]
    return ticker_df


def extract_data(tickers=TICKERS,start_date=START_DATE,end_date=END_DATE)-> dict[str,pd.DataFrame]:

    stock_data={}
    for ticker in tickers:
        df=yf.download(ticker,start=start_date,end=end_date,progress=False)
        if df.empty:
            print(f"No data found for {ticker}")
            continue
        df = process_a_single_ticker(df)
        stock_data[ticker]=df
        #print (stock_data[ticker])
    return stock_data


