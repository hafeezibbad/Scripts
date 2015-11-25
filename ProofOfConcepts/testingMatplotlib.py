#!/usr/bin/python
__author__ = 'eb'

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as pl


# create figure with specified size and ppi
pl.figure(figsize=(8, 6), dpi=72)

# create a new subplot from grid
pl.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cosine, sine = np.cos(X),np.sin(X)

# plot cosine data
pl.plot(X, cosine, color="blue", linewidth=1.0, linestyle="-", label="cosine")

# plot sine data
pl.plot(X, sine, color="red", linewidth=1.0, linestyle="-", label="sine")

# set limit on x axis
pl.xlim(-4.0, 4.0)
pl.xlim(X.min()*1.2, X.max()*1.2)
# pl.xticks(np.linspace(-4, 4, 9, endpoint=True))
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# set limit on x axis
pl.ylim(-1.0, 1.0)
pl.yticks(np.linspace(-1, 1, 10, endpoint=True))
pl.yticks([-1, 0, 1])
pl.ylim(cosine.min()*1.2, cosine.max()*1.2)


# get current axis
ax = pl.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# legend
pl.legend(loc='upper left')

# making annotations
t = 2 * np.pi / 3
pl.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
pl.scatter([t, ], [np.cos(t), ], 50, color='blue')
pl.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
            xy=(t, np.sin(t)), xycoords='data',
            xytext=(+10, +30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

pl.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
pl.scatter([t, ], [np.sin(t), ], 50, color='red')

pl.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
            xy=(t, np.cos(t)), xycoords='data',
            xytext=(-90, -50), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# set the details (Artists+BBox)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
pl.show()
