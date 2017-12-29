'''
@author Sam
@date 2017-12-29
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习排列和随机采样
np.random.permutation(5)函数可以轻松的实现对Serices和DataFrame的列的排列工作

'''

import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(5*4).reshape(5,4))
sampler = np.random.permutation(5)
print(sampler)

df = df.take(sampler)
print(df)
tmp = df.take(np.random.permutation(len(df)))[:3]
print('================>我就是分隔线 1 <==============')
print(tmp)
