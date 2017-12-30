'''
@author Sam
@date 2017-12-29
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习计算指标/哑变量
另一种常用于统计建模或机器学习的转换方式是：将分类变量转换为哑变量矩阵或指标矩阵。
如果DataFrame的某一列中含有k个不同的值，则可以派出一个k列矩阵或DataFrame
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})
print(df)
print(pd.get_dummies(df['key']))

print('================>我就是分隔线 1 <==============')
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)