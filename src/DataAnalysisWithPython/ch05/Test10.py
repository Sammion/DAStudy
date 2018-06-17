'''
@author Sam
@date 2017-12-25
@des 第五章pandas入门
这里主要练习缺失数据处理。
但部分数据分析应用中很常见。pandas的设计目标之一就是让缺失数据的处理任务尽量轻松。例如，pandas对象上的所有描述统计都排除了缺失数据。

'''

import pandas as pd
import numpy as np
from numpy import nan as NA

string_data = pd.Series(['hello', 'world', 'C++', 'Python', np.NaN, 'css'])
print(string_data)
print(string_data.isnull())
print('================>我就是分隔线 1 <==============')
print(string_data.fillna('Not a number'))
print('================>我就是分隔线 2 <==============')
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()
print(data.dropna())
print('================>我就是分隔线 3 <==============')
print(data[data.notnull()])
print('================>我就是分隔线 4 <==============')
data = pd.DataFrame([[1, 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
cleandata = data.dropna()
print(data)
print(cleandata)
print('================>我就是分隔线 5 <==============')
cleandata = data.dropna(how='all')
print(data)
print(cleandata)
print('================>我就是分隔线 6 <==============')
data[4] = NA
print(data)
print(data.dropna(axis=1, how='all'))
print('================>我就是分隔线 7 <==============')
df = pd.DataFrame(np.random.randn(12, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print(df)
print(df.dropna(thresh=3))
