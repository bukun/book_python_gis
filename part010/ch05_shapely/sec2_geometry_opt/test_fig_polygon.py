'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch

from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

from figures import BLUE, SIZE, set_limits, plot_coords, color_isvalid

fig = pyplot.figure(1, figsize=(13, SIZE[1]), dpi=90)

# 1: valid polygon
ax = fig.add_subplot(131)

ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int = [(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]
polygon = Polygon(ext, [int])

plot_coords(ax, polygon.interiors[0])
plot_coords(ax, polygon.exterior)

patch = PolygonPatch(polygon, facecolor=color_isvalid(polygon), edgecolor=color_isvalid(polygon, valid=BLUE), alpha=0.5,
                     zorder=2)
ax.add_patch(patch)

ax.set_title('a) 有效', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 2: invalid self-touching ring
ax = fig.add_subplot(132)
ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int = [(1, 0), (0, 1), (0.5, 1.5), (1.5, 0.5), (1, 0)][::-1]
polygon = Polygon(ext, [int])

plot_coords(ax, polygon.interiors[0])
plot_coords(ax, polygon.exterior)

patch = PolygonPatch(polygon, facecolor=color_isvalid(polygon), edgecolor=color_isvalid(polygon, valid=BLUE), alpha=0.5,
                     zorder=2)
ax.add_patch(patch)

ax.set_title('b) 无效',  fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# pyplot.show()


# 3: invalid polygon, ring touch along a line
ax = fig.add_subplot(133)

ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int = [(0.5, 0), (1.5, 0), (1.5, 1), (0.5, 1), (0.5, 0)]
polygon = Polygon(ext, [int])

plot_coords(ax, polygon.interiors[0])
plot_coords(ax, polygon.exterior)

patch = PolygonPatch(polygon, facecolor=color_isvalid(polygon), edgecolor=color_isvalid(polygon, valid=BLUE), alpha=0.5,
                     zorder=2)
ax.add_patch(patch)

ax.set_title('c) 无效', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# # 4: invalid self-touching ring
# ax = fig.add_subplot(144)
# ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
# int_1 = [(0.5, 0.25), (1.5, 0.25), (1.5, 1.25), (0.5, 1.25), (0.5, 0.25)]
# int_2 = [(0.5, 1.25), (1, 1.25), (1, 1.75), (0.5, 1.75)]
# # int_2 = [
# polygon = Polygon(ext, [int_1, int_2])
#
# plot_coords(ax, polygon.interiors[0])
# plot_coords(ax, polygon.interiors[1])
# plot_coords(ax, polygon.exterior)
#
# patch = PolygonPatch(polygon, facecolor=color_isvalid(polygon), edgecolor=color_isvalid(polygon, valid=BLUE), alpha=0.5,
#                      zorder=2)
# ax.add_patch(patch)
#
# ax.set_title('d) 有效', fontproperties=font_song)
#
# set_limits(ax, -1, 3, -1, 3)

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
