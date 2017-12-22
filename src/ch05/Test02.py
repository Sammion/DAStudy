'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下DataFram数据结构的花式创建、查询
DF是一个表格形的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）。
它既有行索引，也有列索引，可以被看做有Series组成的字典。
它面向行和列的操作时平衡的，实际上，DF中的数据是以一个或者多个二维块存的。
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'state': ['hello', 'good', 'morning'],
        'year': [1991, 1993, 1995],
        'pop': [1, 2.3, 4]}
frame = pd.DataFrame(data=data)
print(frame)
print('================>我就是分割线<==============')
print(pd.DataFrame(data, columns=['year', 'pop']))
print('================>我就是分割线<==============')
frame2 = pd.DataFrame(data, columns=['year', 'pop', 'state', 'debt'], index=['one', 'two', 'three'])
print(frame2)
print('================>我就是分割线<==============')
print(frame2.columns)
print('================>我就是分割线<==============')
print(frame2['state'])
print('================>我就是分割线<==============')
print(frame2['year'])
print(frame2.year)
print('================>我就是分割线<==============')
print(frame2.ix['three'])
print('================>我就是分割线<==============')
frame2.debt = np.arange(3.0)
print(frame2)
print('================>我就是分割线<==============')
val = pd.Series(['-1', '-3', '4'], index=['two', 'three', 'one'])
frame2.debt = val
print(frame2)
print('================>我就是分割线<==============')

frame2['new'] = val
print(frame2)
print('================>我就是分割线<==============')
del frame2['new']
print(frame2)
print('================>我就是分割线<==============')
pop = {'Nevada': {2001: 32, 2002: 34}, 'Sam': {200: 12, 2001: 90, 2003: 1098}}
frame3 = pd.DataFrame(pop)
print(frame3)
print('================>我就是分割线<==============')
print(frame3.T)
print('================>我就是分割线<==============')
frame3 = pd.DataFrame(pop, index=[2001, 2003, 2002, 200])
print(frame3)
print('================>我就是分割线<==============')
frame3.index.name = 'year'
frame3.columns.name = 'cols'
print(frame3)
print('================>我就是分割线<==============')
print(frame3.values)