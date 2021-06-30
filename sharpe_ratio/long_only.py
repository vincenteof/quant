# sharpe ratio of long-only strategy for IGE

import pandas as pd
import math

DAYS = 252

ige = pd.read_excel('./data_files/IGE.xls', index_col=0)
ige.rename(index=pd.to_datetime, inplace=True)
ige.sort_index(inplace=True)
# compare to prev day close
daily_ret = ige['Adj Close'].diff() / ige['Adj Close'].shift(periods=1)
excess_daily_ret = daily_ret - 0.04 / DAYS
sharpe_ratio = math.sqrt(
    DAYS) * excess_daily_ret.mean(axis=0) / excess_daily_ret.std(axis=0)
print(sharpe_ratio)
