'''
@author Sam
@date 2017-12-27
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习去除重复数据
去除重复数据
'''

import pandas as pd
import numpy as np

print('================>我就是分隔线 4 <==============')
data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
tmp = data.duplicated()
print(tmp)
print('================>我就是分隔线 5 <==============')
tmp = data.drop_duplicates()
print(tmp)
print('================>我就是分隔线 6 <==============')
data['v1'] = range(7)
tmp = data.drop_duplicates(['k1'])
print(tmp)
print('================>我就是分隔线 7 <==============')
tmp = data.drop_duplicates(['k1','k2'], keep='last')
print(tmp)