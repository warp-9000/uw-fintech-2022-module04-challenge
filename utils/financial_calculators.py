
import pandas as pd

"""A function for calculating returns from a Pandas DataFrame object
    
    pandas_df: the dataframe from which to calculate the return
    period: (default = 1) the number of days in which to calculate the return
    
"""
def calculate_returns(pandas_df, period=1, dropna=True):
    
    # Create the returns dataframe from the dataframe provided using the shift function
    returns_df = pandas_df.pct_change(periods=period)
    
    if dropna:
        returns_df.dropna(inplace=True)
    
    return returns_df


"""A function for calculating cumulative returns from a Pandas DataFrame object

    pandas_df: the dataframe from which to calculate the return
    
"""
def calculate_cumulative_returns(daily_returns_df):
    
    returns_df = (1 + daily_returns_df).cumprod()
    
    return returns_df