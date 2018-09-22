from matplotlib import pyplot
from shapely.geometry import MultiPolygon
from descartes.patch import PolygonPatch

from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

from figures import BLUE, SIZE, set_limits, plot_coords, color_isvalid

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1: valid multi-polygon
ax = fig.add_subplot(121)

a = [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]
b = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]

multi1 = MultiPolygon([[a, []], [b, []]])

for polygon in multi1:
    plot_coords(ax, polygon.exterior)
    patch = PolygonPatch(polygon, facecolor=color_isvalid(multi1), edgecolor=color_isvalid(multi1, valid=BLUE),
                         alpha=0.5, zorder=2)
    ax.add_patch(patch)

ax.set_title('a) 有效', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 2: invalid self-touching ring
ax = fig.add_subplot(122)

c = [(0, 0), (0, 1.5), (1, 1.5), (1, 0), (0, 0)]
d = [(1, 0.5), (1, 2), (2, 2), (2, 0.5), (1, 0.5)]

multi2 = MultiPolygon([[c, []], [d, []]])

for polygon in multi2:
    plot_coords(ax, polygon.exterior)
    patch = PolygonPatch(polygon, facecolor=color_isvalid(multi2), edgecolor=color_isvalid(multi2, valid=BLUE),
                         alpha=0.5, zorder=2)
    ax.add_patch(patch)

ax.set_title('b) 无效', fontproperties=font_song)

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
