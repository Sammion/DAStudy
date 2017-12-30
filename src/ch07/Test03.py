'''
@author Sam
@date 2017-12-27
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习重塑层次化索引
stack 将数据的列旋转为行
unstack 将数据的行旋转为列

'''
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape(2, 3), index=pd.Index(['Nanjing', 'Beijing'], name='City'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)
print('================>我就是分隔线 1 <==============')
tmp = data.stack()
print(tmp)
print('================>我就是分隔线 2 <==============')
tmp = data.unstack()
print(tmp)
print('================>我就是分隔线 3 <==============')
# pivoted = data.pivot('date', 'item', 'value')
print('pandas 可以实现数据库的行转列。使用pivot,但是pivot只是一个快捷方式，set_index创建层次化索引，再用Unstack进行重塑')

