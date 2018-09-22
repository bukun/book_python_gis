'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry import Point
from shapely.ops import cascaded_union
from descartes import PolygonPatch

from matplotlib.font_manager import FontProperties
font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")


from figures import SIZE, BLUE, GRAY, set_limits

polygons = [Point(i, 0).buffer(0.7) for i in range(5)]

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1
ax = fig.add_subplot(121)

for ob in polygons:
    p = PolygonPatch(ob, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
    ax.add_patch(p)

ax.set_title('a) 多边形',  fontproperties=font_song)

set_limits(ax, -2, 6, -2, 2)

# 2
ax = fig.add_subplot(122)

u = cascaded_union(polygons)
patch2b = PolygonPatch(u, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch2b)

ax.set_title('b) 合并结果',   fontproperties=font_song)

set_limits(ax, -2, 6, -2, 2)

# pyplot.show()

import os

pyplot.savefig(os.path.join(
    os.path.dirname(__file__),
    'xx{bname}.pdf'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )
),bbox_inches='tight')

pyplot.savefig(os.path.join(
    os.path.dirname(__file__),
    'xx{bname}.png'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )
),bbox_inches='tight')
pyplot.clf()
