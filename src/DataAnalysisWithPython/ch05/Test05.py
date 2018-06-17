'''
@author Sam
@date 2017-12-22
@des 第五章pandas入门
这里主要练习一下函数应用和映射。

'''

import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))
print('================>我就是分隔线1<==============')
f = lambda x: x.max() - x.min()
print(frame.apply(f))
print('================>我就是分隔线2<==============')
print(frame.apply(f, axis=1))
print('================>我就是分隔线3<==============')
print(frame.apply(f, axis=0))
print('================>我就是分隔线4<==============')
print(frame)
format = lambda x: '%.2f' % x
print(frame.applymap(format))
print('================>我就是分隔线5<==============')
print(frame['e'].map(format))
