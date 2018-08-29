'''
@author Sam
@date 2018-01-02
@des 第八章 数据可视化
这里主要练习Matplotlib的颜色标记和线型

'''

from numpy.random import random
import matplotlib.pyplot as plt
import numpy as np

# plt.plot(np.arange(30)*10, random(30), 'ko--')
data = (random(30) * 10).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'r-', drawstyle='steps-post', label='Steps-post')
plt.legend(loc='upper center')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(random(1000).cumsum())
ax.set_xticks([0, 250, 500, 800, 1000])
ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
ax.set_title('My title!')
ax.set_xlabel('stages')
ax.set_ylabel(r'片')
plt.show()
