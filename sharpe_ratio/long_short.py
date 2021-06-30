# long-short market-neutral strategy

import pandas as pd
import math


DAYS = 252

ige = pd.read_excel('./data_files/IGE.xls', index_col=0)
spy = pd.read_excel('./data_files/SPY.xls', index_col=0)

ige.rename(index=pd.to_datetime, inplace=True)
spy.rename(index=pd.to_datetime, inplace=True)

ige.sort_index(inplace=True)
spy.sort_index(inplace=True)

ige_daily_ret = ige['Adj Close'].diff() / ige['Adj Close'].shift(periods=1)
spy_daily_ret = spy['Adj Close'].diff() / spy['Adj Close'].shift(periods=1)

net_ret = (ige_daily_ret - spy_daily_ret) / 2

sharpe_ratio = math.sqrt(
    DAYS) * net_ret.mean(axis=0) / net_ret.std(axis=0)

print(sharpe_ratio)
