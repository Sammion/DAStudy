'''
@author Sam
@date 2017-12-25
@des 第五章pandas入门
这里主要练习层次化索引。
层次化索引是pandas的重要功能， 它是你能在一个轴上拥有多个索引级别。
抽象点说，它使你能以低维度形式处理高维度数据。
'''

import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(10),
                 index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data.index)

print('================>我就是分隔线 1 <==============')
print(data['a':'c'])
print('================>我就是分隔线 2 <==============')
print(data.ix[['b', 'c']])
print('================>我就是分隔线 3 <==============')
print(data[:, 2])
print('================>我就是分隔线 4 <==============')
print(data['a', 2])
print('================>我就是分隔线 5 <==============')

data_df = data.unstack()
print(data_df)
print('================>我就是分隔线 6 <==============')
data_df = data.unstack().stack()
print(data_df)

print('================>我就是分隔线 7 <==============')
frame = pd.DataFrame(np.random.randn(12).reshape(4, 3), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['L', 'L', 'S'], ['C++', 'Python', 'Java']])
print(frame)
print('================>我就是分隔线 8 <==============')
frame.index.names = ['key1', 'key2']
frame.columns.names = ['Style', 'name']
print(frame)
print(frame['L'])
print(frame.L)
print('================>我就是分隔线 9 <==============')
print(frame)
frame.swaplevel('key1', 'key2')
print(frame.swaplevel('key1', 'key2'))
print('================>我就是分隔线 10 <==============')
print(frame.swaplevel('key1', 'key2').sort_index(level='key2'))
print('================>我就是分隔线 11 <==============')
print(frame.sum(level='key2'))
print(frame.sum(level='key1'))
# print(frame.sum(level='L', axis=1))