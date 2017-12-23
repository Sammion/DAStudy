'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下Index索引对象
pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。

'''

import pandas as pd
import numpy as np

obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj)
print('================>我就是分割线<==============')
data = {'state': ['hello', 'good', 'morning'],
        'year': [1991, 1993, 1995],
        'pop': [1, 2.3, 4]}
frame = pd.DataFrame(data=data)
print(frame)
print('year' in frame.columns)
print('a' in frame.index)
print('================>我就是分割线<==============')
obj2 = obj.reindex(['c', 'b', 'a', 'd'])
print(obj2)
print('================>我就是分割线<==============')
obj2 = obj.reindex(['c', 'b', 'a', 'd'], fill_value=0.0)
print(obj2)
print('================>我就是分割线<==============')
obj2 = obj.reindex(['c', 'b', 'a', 'd'], method='ffill')
print(obj2)
print('================>我就是分割线<==============')
state = ['a', 'b', 'c']
print(frame.reindex(columns=['pop']))
frame2 = frame.reindex(index=[2, 1, 3, 0])
print(frame2)
frame2 = frame.reindex(index=[2, 1, 3, 0], method='ffill')
print(frame2)
print('================>我就是分割线<==============')
frame3 = frame2.drop(3)
print(frame3)
print('================>我就是分割线<==============')
obj = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
print(obj['b':'c'])
print(obj[obj >= 2])
print('================>我就是分割线<==============')
print(obj[3:5])

print('================>我就是分割线<==============')
data = {'state': ['hello', 'good', 'morning', 'China', 'English'],
        'year': [1991, 1993, 1995, 2007, 2017],
        'pop': [1, 2.3, -4, 100, 104]}
frame = pd.DataFrame(data=data, index=['one', 'two', 'three', 'four', 'five'])
frame.index.name = 'i'
frame.columns.name = 'cols'
print(frame)
frame2 = frame.ix[['one', 'b', 'v', 'd', 'e'], ['pop', 'state']]

print(frame2)
print('================>我就是分割线<==============')
print(frame[frame['pop'] > 10])
print('================>我就是分割线<==============')
print(frame > 10)
print(frame['pop'] > 10)
print('================>我就是分割线1<==============')
print(frame.ix[['one'], ['pop', 'state']])
print('================>我就是分割线2<==============')
print(frame.ix[['one', 'two']])
print('================>我就是分割线3<==============')
print(frame.ix[['pop', 'state'], ['one', 'two']])
print('================>我就是分割线4<==============')
print(frame.ix[:'three', 'pop'])
print('================>我就是分割线5<==============')
print(frame['pop'])
print(frame.ix[frame['pop'] > 0, :1])
