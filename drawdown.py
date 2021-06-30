# drawdown calculation

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


def calculateMaxDD(cum_ret):
    highwater_mark = np.zeros(cum_ret.shape[0])
    drawdown = np.zeros(cum_ret.shape[0])
    drawdown_duration = np.zeros(cum_ret.shape[0])
    for i in range(1, cum_ret.shape[0]):
        highwater_mark[i] = max(highwater_mark[i - 1], cum_ret[i])
        drawdown[i] = (highwater_mark[i] - cum_ret[i]) / \
            (1 + highwater_mark[i])
        if drawdown[i] == 0:
            drawdown_duration[i] = 0
        else:
            drawdown_duration[i] = drawdown_duration[i - 1] + 1
    return max(drawdown), max(drawdown_duration)


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
# 总资产回报率
cum_ret = (net_ret + 1).cumprod(axis=0) - 1
(max_d, max_dd) = calculateMaxDD(cum_ret)

print(max_d)
print(max_dd)
# plt.plot(np.arange(0, cum_ret.shape[0]), cum_ret.values)
# plt.show()
