'''
@author Sam
@date 2017-12-25
@des 第五章pandas入门
这里主要练习唯一值、值计数及成员资格。
'''

import pandas as pd

obj = pd.Series(list('cadaabbcc'))
uniques = obj.unique()
print(uniques)
print(obj.value_counts())

print('================>我就是分隔线 1 <==============')
print(pd.value_counts(obj.values, sort=False))
print('================>我就是分隔线 2 <==============')
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])
print('================>我就是分隔线 3 <==============')
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
print('================>我就是分隔线 4 <==============')
result = data.apply(pd.value_counts).fillna(0)
print(result)