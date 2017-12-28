'''
@author Sam
@date 2017-12-28
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习重命名轴索引
根Series中的值一样，轴标签也可以通过函数或映射进行转换，
从而得到一个新对象轴还可以被就地修改，而无需新建一个数据结构。
'''

import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                    index=['Nanjing', 'Beijing', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print('================>我就是分隔线 1 <==============')
print(data.index.map(str.upper))
print('================>我就是分隔线 2 <==============')
print(data.rename(index=str.title, columns=str.upper))

print('================>我就是分隔线 3 <==============')
print(data.rename(index={'Nanjing':'Hujian'}, columns={'one':1,'two':2}))