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
print('================>我就是分隔线 1<==============')
obj = obj.sort_index()
print(obj)
tmp = sorted(obj)
print(tmp)














