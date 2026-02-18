import pandas as pd 
from datetime import datetime
def change_name(df: pd.DataFrame) -> pd.DataFrame:
    df=df.rename(columns={"Date":"ds","Close":"y"})
    return df

  
def prepare_data_for_prophet(stock_data: dict[str,pd.DataFrame])->dict[str,pd.DataFrame]:
    prepared_data={}
    for ticker in stock_data:
        df=stock_data[ticker]
        df=change_name(df)
        prepared_data[ticker]=df
    return prepared_data


  