'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下算术运算和数据对齐。

'''

import pandas as pd
import numpy as np

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'd'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

data = {'state': ['hello', 'good', 'morning', 'China', 'English'],
        'year': [1991, 1993, 1995, 2007, 2017],
        'pop': [1, 2.3, -4, 100, 104]}
frame = pd.DataFrame(data=data, index=['one', 'two', 'three', 'four', 'five'])
print(s1)
print(s2)
print('================>我就是分隔线1<==============')
s = s1 + s2
print(s)
print('================>我就是分隔线2<==============')
df1 = pd.DataFrame(np.arange(9.0).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.0).reshape((4, 3)), columns=list('dbe'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
print('================>我就是分隔线3<==============')
df = df1 + df2
print(df)
print('================>我就是分隔线4<==============')
df1 = pd.DataFrame(np.arange(12.0).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.0).reshape((4, 5)), columns=list('abcde'))
print(df1)
print(df2)
df = df1 + df2
print('================>我就是分隔线5<==============')
print(df1.add(df2, fill_value=0))
print(df2.sub(df1, fill_value=0))

print('================>我就是分隔线6<==============')
arr = np.arange(12.0).reshape((3, 4))
print(arr)
print(arr[0])
print('================>我就是分隔线7<==============')
frame = pd.DataFrame(np.arange(12.0).reshape(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]
print(series)
print(frame)
print(frame - series)
print('================>我就是分隔线8<==============')
print(arr - arr[0])
print('================>我就是分隔线9<==============')
series2 = pd.Series(range(1, 4), index=['b', 'e', 'f'])
print(frame + series2)
print(frame / series2)
print('================>我就是分隔线10<==============')

series3 = frame['d']
print(series3)
print(frame.sub(series3, axis=0))
series4 = frame.ix['Utah']
print(frame.sub(series4, axis=1))
