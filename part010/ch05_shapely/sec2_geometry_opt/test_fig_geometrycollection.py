'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry import LineString
from figures import BLUE, GRAY, YELLOW, GREEN, SIZE, set_limits, plot_coords, BLACK

from matplotlib.font_manager import FontProperties
font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

pyplot.clf()

fig = pyplot.figure(1, figsize=SIZE, dpi=90)  # 1, figsize=(10, 4), dpi=180)

a = LineString([(0, 0), (1, 1), (1, 2), (2, 2)])
b = LineString([(0, 0), (1, 1), (2, 1), (2, 2)])

# 1: disconnected multilinestring
ax = fig.add_subplot(131)

plot_coords(ax, a)
# plot_coords(ax, b)

x, y = a.xy
ax.plot(x, y,  color=GRAY, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

# x, y = b.xy
# ax.plot(x, y, color=GREEN, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('a) 线a', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 1: disconnected multilinestring
ax = fig.add_subplot(132)

# plot_coords(ax, a)
plot_coords(ax, b)

# x, y = a.xy
# ax.plot(x, y, color=YELLOW, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

x, y = b.xy
ax.plot(x, y,  color=GRAY,alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('b) 线b',  fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)


# 2: invalid self-touching ring
ax = fig.add_subplot(133)

# x, y = a.xy
# ax.plot(x, y,  alpha=0.7, linewidth=1, solid_capstyle='round', zorder=1)
# x, y = b.xy
# ax.plot(x, y, color=GRAY, alpha=0.7, linewidth=1, solid_capstyle='round', zorder=1)

for ob in a.intersection(b):
    x, y = ob.xy
    if len(x) == 1:
        ax.plot(x, y, 'o', color=GRAY, zorder=2)
    else:
        ax.plot(x, y,  alpha=0.7, color=GRAY,linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('c) 线a与线b相交生成的集合', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# pyplot.show()

import os

plt = pyplot
plt.savefig(os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'xx{bname}.pdf'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )), bbox_inches='tight')

plt.savefig(os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'xx{bname}.png'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )) , bbox_inches='tight')
pyplot.clf()
