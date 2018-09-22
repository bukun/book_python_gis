from matplotlib import pyplot
from shapely.geometry import MultiPoint

from descartes.patch import PolygonPatch
from matplotlib.font_manager import FontProperties
font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")
# from pygiser import GRAY, BLUE, set_limits, plot_line
from figures import SIZE, BLUE, GRAY, plot_line, set_limits, DARKGRAY

fig = pyplot.figure(1, figsize=SIZE, dpi=90)
fig.set_frameon(True)

# 1
ax = fig.add_subplot(121)

points2 = MultiPoint([(0, 0), (2, 2)])
for p in points2:
    ax.plot(p.x, p.y, 'o', color=DARKGRAY)
hull2 = points2.convex_hull
plot_line(ax, hull2, color=GRAY, alpha=0.5, zorder=2)

ax.set_title('a) N = 2')

set_limits(ax, -1, 4, -1, 3)

# 2
ax = fig.add_subplot(122)

points1 = MultiPoint([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

for p in points1:
    ax.plot(p.x, p.y, 'o', color=DARKGRAY)
hull1 = points1.convex_hull
patch1 = PolygonPatch(hull1, facecolor=GRAY, edgecolor=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch1)

ax.set_title('b) N > 2')

set_limits(ax, -1, 4, -1, 3)

# pyplot.show()

plt = pyplot
import os

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0],
                         'xx{bname}.pdf'.format(
                             bname=os.path.splitext(os.path.basename(__file__))[0][4:]
                         )
                         ), bbox_inches='tight')

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0],
                         'xx{bname}.png'.format(
                             bname=os.path.splitext(os.path.basename(__file__))[0][4:]
                         )
                         ), bbox_inches='tight')
plt.clf()
plt.close()
