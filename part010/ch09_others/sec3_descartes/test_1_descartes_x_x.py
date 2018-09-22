# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
from matplotlib import pyplot as plt
from shapely.geometry import LineString
from descartes import PolygonPatch
BLUE = '#6699cc'
GRAY = '#999999'
################################################################################
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)
################################################################################
def set_limits(ax, x0, xN, y0, yN):
    ax.set_xlim(x0, xN)
    ax.set_xticks(range(x0, xN+1))
    ax.set_ylim(y0, yN)
    ax.set_yticks(range(y0, yN+1))
    ax.set_aspect("equal")
################################################################################
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
################################################################################
fig = plt.figure(1, figsize=(10, 4), dpi=180)
ax = fig.add_subplot(121)
set_limits(ax, -1, 4, -1, 3)
plot_line(ax, line)
################################################################################
dilated = line.buffer(0.5)
patch1 = PolygonPatch(dilated, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
ax.add_patch(patch1)
################################################################################
ax = fig.add_subplot(122)
patch2a = PolygonPatch(dilated, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
ax.add_patch(patch2a)
set_limits(ax, -1, 4, -1, 3)
################################################################################
eroded = dilated.buffer(-0.3)
polygon = eroded.__geo_interface__
################################################################################
patch2b = PolygonPatch(polygon, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch2b)

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
