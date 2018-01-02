'''
@author Sam
@date 2018-01-02
@des 第七章 数据可视化
这里主要练习Matplotlib的间距调整
Figure 和 Subplots
'''

import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

# 一次对figure对象和ax对象赋值
fig, axes = plt.subplots(3, 2, sharex=True, sharey=True)
#
plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8, wspace=0, hspace=0)
axes[0][1].spines['bottom'].set_color('green')
axes[0][1].spines['top'].set_color('green')
axes[0][1].spines['left'].set_color('green')
axes[0][1].spines['right'].set_color('green')
for i in range(2):
    for j in range(2):
        axes[i, j].hist(random(500), bins=50, color='b', alpha=0.5)

plt.show()
