'''
@author Sam
@date 2017-12-25
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习合并数据集
pandas.merge 可根据一个或多个建将不同DataFrame中的行连接起来，类似数据库中的连接操作。
pandas.concat 可以沿着一条轴将多个对象堆叠起来，对一个对象中的值填充另一个对象中的缺失值。
'''

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print('================>我就是分隔线 1 <==============')
print(df2)
print('================>我就是分隔线 2 <==============')
print(pd.merge(df1, df2))
print(pd.merge(df1, df2, on='key'))

print('================>我就是分隔线 3 <==============')
df1 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
print(pd.merge(df1, df2, right_on='rkey', left_on='lkey'))
print('================>我就是分隔线 4 <==============')
print(pd.merge(df1, df2, how='outer', right_on='rkey', left_on='lkey'))
print('================>我就是分隔线 5 <==============')
print(pd.merge(df1, df2, how='left', right_on='rkey', left_on='lkey'))
print('================>我就是分隔线 6 <==============')
print(pd.merge(df1, df2, how='right', right_on='rkey', left_on='lkey'))
print('================>我就是分隔线 7 <==============')
print(pd.merge(df1, df2, how='inner', right_on='rkey', left_on='lkey'))

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

print('================>我就是分隔线 8 <==============')
tmp = pd.merge(left, right, on='key1', how='outer', suffixes=('_left', '_right'))
print(tmp)

print('================>我就是分隔线 9 <==============')
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
# print(left1)
tmp = pd.merge(left1, right1, left_on='key', right_index=True)
print(tmp)
print('================>我就是分隔线 10 <==============')
tmp = pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
print(tmp)
print('================>我就是分隔线 11 <==============')
lefth = pd.DataFrame({'key1': ['Beijing', 'Beijing', 'Beijing', 'Nanjing', 'Nanjing'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nanjing', 'Nanjing', 'Beijing', 'Beijing', 'Beijing', 'Beijing'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
print(lefth)
print(righth)
print('================>我就是分隔线 12 <==============')
tmp = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
print(tmp)
print('================>我就是分隔线 13 <==============')
tmp = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')
print(tmp)

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], columns=['Nanjing', 'Beijing'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14.]], index=['b', 'c', 'd', 'e'],
                      columns=['Jiangsu', 'Shandong'])
print(left2)
print(right2)
print('================>我就是分隔线 14 <==============')
tmp = pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
print(tmp)