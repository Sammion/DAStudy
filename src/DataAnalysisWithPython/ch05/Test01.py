'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习Series数据结构的花式创建、查询。
Series 是一种类似于一维数组的对象。
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print(s.values)
print(s.index)

obj2 = pd.Series([1, 3, 4], index=['a', 'd', 'c'])
print(obj2)
print(obj2['a'])
print(obj2.index)
print(obj2[['a', 'c']])
print('=====================================================')
obj2 = obj2 * 2
print(obj2)
print(obj2[obj2 > 5])

print('=====================================================')
obj2 = np.exp(obj2)
print(obj2)

print('=====================================================')
print('a' in obj2)
print('e' in obj2)
print(2 in obj2)
print(7.380956 in obj2)
print('========================我就是分割线=============================')
sdata = {'chi': 12, 'hui': 32, 'ni': 16.32}
obj3 = pd.Series(sdata)
print(obj3)
print('========================我就是分割线=============================')
states = ['hui', 'ni', 'hello']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print('========================我就是分割线=============================')
print(pd.isnull(obj4))
print('========================我就是分割线=============================')
print(pd.notnull(obj4))
print('========================我就是分割线=============================')
print(obj4.isnull())
print('========================我就是分割线=============================')
data1 = {'chi': 12, 'hui': 31, 'ni': 16.32}
data2 = {'chi': 8, 'hello': 32, 'hui': 9}
obj3 = pd.Series(data1)
obj4 = pd.Series(data2)
print(obj3 + obj4)
print('========================我就是分割线=============================')

obj4.index.name = "state"
print(obj4.name)
print(obj4.index.name)

print('========================我就是分割线=============================')
obj_index = ['Hello', 'numpy', 'pandas']
obj4.index = obj_index
print(obj4)
