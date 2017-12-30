'''
@author Sam
@date 2017-12-30
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习USDA食品数据库的数据分析

'''

import json
import pandas as pd

db = json.load(open('foods-2011-10-03.json'))
print(len(db))
print(db[0].keys())
print(db[0].values())
print(type(db))
print(type(db[0]))
print('================>我就是分隔线 1 <==============')
print(db[0]['nutrients'][0])
print('================>我就是分隔线 2 <==============')
nutrients = pd.DataFrame(db[0]['nutrients'])
print(nutrients.tail())
print('================>我就是分隔线 3 <==============')
info_keys = ['description', 'group', 'id', 'manufacturer']
info = pd.DataFrame(db, columns=info_keys)
print(info.tail())
print('================>我就是分隔线 4 <==============')
print(pd.value_counts(info.group[:10]))
print('================>我就是分隔线 5 <==============')
nutrients = []
for res in db:
    fnuts = pd.DataFrame(res['nutrients'])
    fnuts['id'] = res['id']
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients, ignore_index=True)
print(nutrients.tail())
print('================>我就是分隔线 6 <==============')
print(nutrients.duplicated().sum())
# 删除重复项
nutrients = nutrients.drop_duplicates()
# 对列名重命名
col_mapping = {'description': 'food', 'group': 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
col_mapping = {'description': 'nutfood', 'group': 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)

ndata = pd.merge(nutrients, info, on='id', how='outer')
print(ndata.tail())
result = ndata.groupby(['nutrients', 'fgroup'])['value'].quantile(0.5)
result['Zinc,Zn'].order().plot(kind='barh')
