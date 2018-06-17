'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习填充缺失数据。

'''

import pandas as pd
import numpy as np
from numpy import nan as NA

df = pd.DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print(df.fillna(0.00))
print('================>我就是分隔线 1 <==============')
print(df.fillna({1: 0.5, 2: -1}))
print('================>我就是分隔线 2 <==============')
df.fillna(0.12, inplace=True)
print(df)
print('================>我就是分隔线 3 <==============')
df = pd.DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA
df.ix[4:, 2] = NA
# df.fillna(method='bfill')
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=3))
print('================>我就是分隔线 4 <==============')
print(df.mean())
print(df.fillna(df.mean()))