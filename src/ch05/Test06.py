'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下排序和排名。

'''

import pandas as pd
import numpy as np

obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj)
print(obj.sort_index())
sorted(obj)
print('================>我就是分隔线 1 <==============')
obj = obj.sort_index()
print(obj)
tmp = sorted(obj)
print(tmp)
print('================>我就是分隔线 2 <==============')
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), columns=list('dabc'), index=['three', 'one'])
frame1 = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(frame.sort_index())
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))
print('================>我就是分隔线 3 <==============')
print(frame1)
print(frame1.sort_index())
print(frame1.sort_index(axis=1))
print(frame1.sort_index(axis=1, ascending=False))
print('================>我就是分隔线 4 <==============')
obj = pd.Series([4, np.NaN, 7, np.NaN, -3, 2])
# print(obj.sort())
print('================>我就是分隔线 5 <==============')
print(frame1)
print(frame1.sort_values(by='e'))
print(frame1.sort_values(by=['e', 'd']))
print('================>我就是分隔线 6 <==============')
obj1 = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj1.rank())
print('================>我就是分隔线 7 <==============')
print(obj1.rank(method='first'))
print('================>我就是分隔线 8 <==============')
print(obj1.rank(method='max'))
print(obj1.rank(method='max', ascending=False))
print('================>我就是分隔线 9 <==============')
print(frame1)
print(frame1.rank())
print(frame1.rank(axis=1))
print('================>我就是分隔线 10 <==============')
frame2 = pd.DataFrame(np.arange(81).reshape((9, 9)), index=list('adfasdafm'))
print(frame2)
print(frame2.ix['a'])
