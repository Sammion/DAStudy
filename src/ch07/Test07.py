'''
@author Sam
@date 2017-12-28
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习检测和过滤异常值
outlier异常值的过滤或变换运算在很大程度上其实就是数组运算
'''

import pandas as pd
import numpy as np

data = np.random.seed(12345)
data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())
print('================>我就是分隔线 1 <==============')
col = data[3]
print(col[np.abs(col) > 3])
print(data[(np.abs(data) > 3).any(1)])
print('================>我就是分隔线 2 <==============')
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())