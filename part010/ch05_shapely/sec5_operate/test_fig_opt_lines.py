'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry import LineString
from figures import BLUE, GRAY, YELLOW, GREEN, SIZE, set_limits, plot_coords, BLACK

from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

pyplot.clf()

from shapely.ops import polygonize
from shapely.ops import linemerge

fig = pyplot.figure(1, figsize=SIZE, dpi=90)  # 1, figsize=(10, 4), dpi=180)

lines = [((0, 0), (2, 2)),
         ((0, 0), (0, 2)),
         ((0, 2), (2, 2)),
         ((2, 2), (2, 0)),
         ((2, 0), (0, 0))]
the_line = linemerge(lines)
the_poly = polygonize(lines)

# a = LineString([(0, 0), (1, 1), (1, 2), (2, 2)])
# b = LineString([(0, 0), (1, 1), (2, 1), (2, 2)])

# 1: disconnected multilinestring
ax = fig.add_subplot(131)

for x in lines:
    plot_coords(ax, LineString(x))
# plot_coords(ax, b)

# x, y = the_line.xy

xx = [t[0][0] for t in lines]
yy = [t[0][1] for t in lines]

ax.scatter(xx, yy)
# for uu in lines:
#     ax.plot(uu[0][0], uu[0][1],  color=GRAY, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

# x, y = b.xy
# ax.plot(x, y, color=GREEN, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

for x in lines:
    b = LineString(x)
    x, y = b.xy
    ax.plot(x, y, color=GRAY, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('a) 原始的5条线', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 1: disconnected multilinestring
ax = fig.add_subplot(132)

# plot_coords(ax, a)
# plot_coords(ax, the_line)

# x, y = a.xy
# ax.plot(x, y, color=YELLOW, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

for the_l in the_line:
    x, y = the_l.xy
    ax.plot(x, y, color=GRAY, alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('b) 对线进行合并', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 2: invalid self-touching ring
ax = fig.add_subplot(133)

from descartes import PolygonPatch

for ob in the_poly:
    p = PolygonPatch(ob, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
    ax.add_patch(p)

# x, y = a.xy
# ax.plot(x, y,  alpha=0.7, linewidth=1, solid_capstyle='round', zorder=1)
# x, y = b.xy
# ax.plot(x, y, color=GRAY, alpha=0.7, linewidth=1, solid_capstyle='round', zorder=1)

# for the_p in the_poly:
#     plot_coords(ax, the_p)

# for the_l in the_poly:
#     x, y = the_l.xy
#     ax.plot(x, y,  color=GRAY,alpha=0.5, linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('c) 根据线生成多边形', fontproperties=font_song)

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
    )), bbox_inches='tight')
pyplot.clf()
