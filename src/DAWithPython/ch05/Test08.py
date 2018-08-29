'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下相关系数和协方差。
pip install pandas-datareader
'''

import pandas as pd
import numpy as np
from pandas_datareader import data
import pandas_datareader as pdr
import datetime

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = pdr.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
f = data.DataReader("F", 'yahoo', start, end)

# for t in all_data.items():
#     print(t)
price = pd.DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})

volume = pd.DataFrame({tic: data['Volume'] for tic, data in all_data.items()})
returns = price.pct_change()
returns.tail()

returns.MSFT.corr(returns.IBM)
returns.MSFT.cov(returns.IBM)

returns.corr()
returns.cov()

returns.corrwith(returns.IBM)
returns.corrwith(volume)
