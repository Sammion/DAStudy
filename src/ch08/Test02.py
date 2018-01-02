'''
@author Sam
@date 2018-01-02
@des 第八章 数据可视化
这里主要练习Matplotlib绘制Sin Cos
ref: https://www.jianshu.com/p/7fbecf5255f0
'''

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
(C, S) = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)

fig = plt.figure(figsize=(10, 6), dpi=80)
plt.plot(X, C, 'b-', lw=2.5)
plt.plot(X, S, 'r--', lw=2.5)
plt.xlim(X.min() * 1, X.max() * 1)
plt.ylim(C.min() * 1.5, C.max() * 1.5)

plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-1, 0, 1])
# plt.show()

ax = plt.gca()
# 把右边和上边的边界设置为不可见
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
# 然后把下边界和左边界移动到0点
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
plt.plot(X, C, 'b-', lw=2.5, label='cosine')
plt.plot(X, S, 'r--', lw=2.5, label='sine')
plt.legend(loc='upper left')
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='black', linewidth=2.5, linestyle='--')
# 画出需要标注的点
plt.scatter([t, ], [np.cos(t), ], 50, color='green')
# 给这个点加注释
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#
# plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{r\sqr{3}}{2}$',
#              xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
# 同上
plt.plot([t, t], [0, np.sin(t)], color='blue', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.sin(t), ], 50, color='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='w', edgecolor='None', alpha=0.4))
plt.show()
