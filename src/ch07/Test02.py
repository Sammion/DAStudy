'''
@author Sam
@date 2017-12-26
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习轴向连接和合并数据集
pandas.concat 可以沿着一条轴将多个对象堆叠起来，对一个对象中的值填充另一个对象中的缺失值。
'''
import pandas as pd
import numpy as np

arr = np.arange(12).reshape((3, 4))
tmp = np.concatenate([arr, arr], axis=1)
print(tmp)
print('================>我就是分隔线 1 <==============')
tmp = np.concatenate([arr, arr])
print(tmp)
print('================>我就是分隔线 2 <==============')
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
tmp = pd.concat([s1, s2, s3])
print(tmp)
print('================>我就是分隔线 3 <==============')
tmp = pd.concat([s1, s2, s3], axis=1)
print(tmp)

print('================>我就是分隔线 4 <==============')
s4 = pd.concat([s1 * 5, s3])
print(tmp)
print('================>我就是分隔线 5 <==============')
tmp = pd.concat([s1, s4], axis=1, join='inner')
print(tmp)

print('================>我就是分隔线 6 <==============')
tmp = pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
print(tmp)

print('================>我就是分隔线 7 <==============')
tmp = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])
print(tmp)
print(tmp.unstack())

print('================>我就是分隔线 8 <==============')
tmp = pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])
print(tmp)
print('================>我就是分隔线 9 <==============')
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])

tmp = pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
print(tmp)
print('================>我就是分隔线 10 <==============')
tmp = pd.concat({'lvel1':df1, 'level2':df2}, axis=1)
print(tmp)