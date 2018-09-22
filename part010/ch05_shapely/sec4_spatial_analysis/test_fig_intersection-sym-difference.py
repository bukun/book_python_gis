'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry import Point
from descartes import PolygonPatch
from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")
from figures import SIZE, BLUE, GRAY, set_limits, WHITE, BLACK

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)

# 1
ax = fig.add_subplot(121)

patch1 = PolygonPatch(a, fc=WHITE, ec=BLACK, alpha=0.2, zorder=1)
ax.add_patch(patch1)
patch2 = PolygonPatch(b, fc=WHITE, ec=BLACK, alpha=0.2, zorder=1)
ax.add_patch(patch2)
c = a.intersection(b)
patchc = PolygonPatch(c, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patchc)

ax.set_title('a.intersection(b)')

set_limits(ax, -1, 4, -1, 3)

# 2
ax = fig.add_subplot(122)

patch1 = PolygonPatch(a, fc=WHITE, ec=BLACK, alpha=0.2, zorder=1)
ax.add_patch(patch1)
patch2 = PolygonPatch(b, fc=WHITE, ec=BLACK, alpha=0.2, zorder=1)
ax.add_patch(patch2)
c = a.symmetric_difference(b)

if c.geom_type == 'Polygon':
    patchc = PolygonPatch(c, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
    ax.add_patch(patchc)
elif c.geom_type == 'MultiPolygon':
    for p in c:
        patchp = PolygonPatch(p, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
        ax.add_patch(patchp)

ax.set_title('a.symmetric_difference(b)')

set_limits(ax, -1, 4, -1, 3)

# pyplot.show()

import os

plt = pyplot

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

pyplot.clf()
