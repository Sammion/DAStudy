'''
@author Sam
@date 2018-01-03
@des 第八章 数据可视化
这里主要练习pandas绘图工具
'''

from datetime import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from io import StringIO

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=['A', 'B', 'C', 'D'],
                  index=np.arange(0, 100, 10))
fig, axes = plt.subplots(2, 1)
df.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
df.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
# plt.show()


tips = pd.read_csv('tips.csv')
party_counts = pd.crosstab(tips.day, tips.size)
print(party_counts)
# party_counts = party_counts.ix[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
print(party_pcts)
party_pcts.plot(kind='bar', stacked=True)
plt.show()
