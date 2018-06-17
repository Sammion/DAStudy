'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下汇总和计算描述统计。

'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 4), index=list('bcd'), columns=list('abcd'))
print(df)
print('================>我就是分隔线 1 <==============')
print(df.sum())
print(df.sum(axis=1))
print('================>我就是分隔线 2 <==============')
df1 = df.reindex(columns=list('asdcd'))
print(df1)
print(df1.mean(axis=1))
print(df1.mean(axis=1, skipna=False))
print('================>我就是分隔线 3 <==============')
df = pd.DataFrame(np.arange(12.0).reshape(3, 4), index=list('bcd'), columns=list('abcd'))
print(df)
print(df.idxmax())
print(df.idxmin())
print(df.cumsum())
print(np.max(df.a))
print('================>我就是分隔线 4 <==============')
print(df.describe())
obj = pd.Series(['a', 23, 'b', 'a', 'c', 23, 1.0])
print(obj.describe())
print('================>我就是分隔线 5 <==============')
