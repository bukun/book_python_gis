'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry.polygon import LinearRing

from figures import SIZE, set_limits, plot_coords, plot_line_isvalid

from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1: valid ring
ax = fig.add_subplot(121)
ring = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)])

plot_coords(ax, ring)
plot_line_isvalid(ax, ring, alpha=0.7)

ax.set_title('a) 有效', fontproperties=font_song)

set_limits(ax, -1, 3, -1, 3)

# 2: invalid self-touching ring
ax = fig.add_subplot(122)
ring2 = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 1), (0, 0)])

plot_coords(ax, ring2)
plot_line_isvalid(ax, ring2, alpha=0.7)

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
