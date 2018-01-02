'''
@author Sam
@date 2018-01-02
@des 第八章 数据可视化
这里主要练习Matplotlib创建canvas 
Figure 和 Subplot
'''

import pandas as pd
import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

fg = plt.figure()
ax1 = fg.add_subplot(2, 2, 1)
ax2 = fg.add_subplot(2, 2, 2)
ax3 = fg.add_subplot(2, 2, 3)
# 默认使用最后一个子图
plt.plot(random(500), 'k--')
ax1.hist(random(1000), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * random(30))
# 同时创建figure和ax子图对象
# fig, axes = plt.subplot(2, 3)


plt.show()
