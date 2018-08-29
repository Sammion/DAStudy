'''
@author Sam
@date 2017-12-28
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习离散化和面元划分
将数据分组，使用pd.cut函数划分不同的组

'''

import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 23, 21, 37, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
print('================>我就是分隔线 1 <==============')
print(cats.codes)
# print(cats.levels)
print('================>我就是分隔线 2 <==============')
print(pd.value_counts(cats))
print('================>我就是分隔线 3 <==============')
cats = pd.cut(ages, [18, 26, 36, 61, 100], right=False)
print(pd.value_counts(cats))
print('================>我就是分隔线 4 <==============')
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
cats = pd.cut(ages, bins, labels=group_names)
print(cats)
print('================>我就是分隔线 5 <==============')
data = np.random.rand(20)
print(data)
cats = pd.cut(data, 4, precision=2)
print(pd.value_counts(cats))
print('================>我就是分隔线 6 <==============')
data = np.random.rand(1000)
cats = pd.qcut(data, 4)
print(pd.value_counts(cats))

print('================>我就是分隔线 7 <==============')
cats = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
print(pd.value_counts(cats))
