from matplotlib import pyplot
from shapely.geometry import LineString
from descartes import PolygonPatch

from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

# from pygiser import BLUE, GRAY, set_limits, plot_line
from figures import SIZE, BLUE, GRAY, plot_line, set_limits, BLACK, DARKGRAY

line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1
ax = fig.add_subplot(121)

plot_line(ax, line)

dilated = line.buffer(0.5, cap_style=3)
patch1 = PolygonPatch(dilated, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch1)

ax.set_title('a) 膨胀', fontproperties=font_song)  # , cap_style=3

set_limits(ax, -1, 4, -1, 3)

# 2
ax = fig.add_subplot(122)

patch2a = PolygonPatch(dilated, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
ax.add_patch(patch2a)

eroded = dilated.buffer(-0.3)

# GeoJSON-like data works as well

polygon = eroded.__geo_interface__
# >>> geo['type']
# 'Polygon'
# >>> geo['coordinates'][0][:2]
# ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))
patch2b = PolygonPatch(polygon, fc=DARKGRAY, ec=DARKGRAY, alpha=0.5, zorder=2)
ax.add_patch(patch2b)

ax.set_title('b) 腐蚀', fontproperties=font_song)  # join_style=1

set_limits(ax, -1, 4, -1, 3)

# pyplot.show()

plt = pyplot
import os

plt.savefig(os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'xx{bname}.pdf'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )
), bbox_inches='tight')

plt.savefig(os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'xx{bname}.png'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )
), bbox_inches='tight')
plt.clf()
plt.close()
