from matplotlib import pyplot
from shapely.geometry import MultiPoint, Point
from descartes.patch import PolygonPatch

# from pygiser import BLUE, GRAY, set_limits
from figures import SIZE, BLUE, GRAY, WHITE,BLACK, set_limits
from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

fig = pyplot.figure(1, figsize=SIZE, dpi=90)  # 1, figsize=SIZE, dpi=90)

p = Point(1, 1).buffer(1.5)

# 1
ax = fig.add_subplot(121)

q = p.simplify(0.2)

patch1a = PolygonPatch(p, facecolor=WHITE, edgecolor=BLACK, alpha=0.5, zorder=1)
ax.add_patch(patch1a)

patch1b = PolygonPatch(q, facecolor=GRAY, edgecolor=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch1b)

ax.set_title('a) 容差值为 0.2', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 2
ax = fig.add_subplot(122)

r = p.simplify(0.5)

patch2a = PolygonPatch(p, facecolor=WHITE, edgecolor=BLACK, alpha=0.5, zorder=1)
ax.add_patch(patch2a)

patch2b = PolygonPatch(r, facecolor=GRAY, edgecolor=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch2b)

ax.set_title('b) 容差值为 0.5', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

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
