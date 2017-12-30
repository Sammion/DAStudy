'''
@author Sam
@date 2017-12-27
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习去除重复数据
去除DataFrame里的重复数据

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
tmp = data.drop_duplicates(['k1', 'k2'], keep='last')
print(tmp)
print('================>我就是分隔线 8 <==============')
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami',
                              'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}
print('================>我就是分隔线 9 <==============')
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data)
print('================>我就是分隔线 10 <==============')
data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])
print(data)
print('================>我就是分隔线 10 <==============')

obj = pd.Series([1, -999, 2, 3, -999, -1000, 2])
tmp = obj.replace(-999, np.nan)
print(tmp)
print('================>我就是分隔线 11 <==============')
tmp = obj.replace([-999, 1], np.nan)
print(tmp)
print('================>我就是分隔线 12 <==============')
tmp = obj.replace([-999, 1], [np.nan, 0])
print(tmp)
print('================>我就是分隔线 13 <==============')
tmp = obj.replace({-999: np.nan, 2: 200.})
print(tmp)
