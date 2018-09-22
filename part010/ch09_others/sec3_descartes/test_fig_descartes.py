from helper.textool import get_tmp_file

from matplotlib import pyplot as plt
from shapely.geometry import *
from descartes import PolygonPatch

# Create a matplotlib figure
fig = plt.figure(num=1, figsize=(10, 4), dpi=180)
# Create a polygon with 2 holes using buffer and difference methods
polygon = Point(0, 0).buffer(10.0).difference(
    MultiPoint([(-5, 0), (5, 0)]).buffer(3.0))
# 1
# Create a subplot
ax = fig.add_subplot(221)
# Make the polygon into a patch and add it to the subplot
patch = PolygonPatch(polygon, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
# Fit the figure around the polygon's bounds, render, and save
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
ax.set_aspect(1)
# 2
# Create a subplot
ax = fig.add_subplot(222)
# Turn the GeoJSON-ish dict form of the polygon from #1 into a patch
geo = polygon.__geo_interface__
patch = PolygonPatch(geo, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
# Fit the figure around the polygon's bounds, render, and save
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
ax.set_aspect(1)
# Create a multi-polygon with 2 holes and 2 satelite polygons using buffer,
#   difference and union methods
multipolygon = Point(0, 0).buffer(10.0).difference(
    MultiPoint([(-5, 0), (5, 0)]).buffer(3.0)).union(
    MultiPoint([(-10, 10), (10, -10)]).buffer(2.0))
# 3
# Create a subplot
ax = fig.add_subplot(223)
# Make the polygon into a patch and add it to the subplot
patch = PolygonPatch(multipolygon, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
# Fit the figure around the polygon's bounds, render, and save
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
ax.set_aspect(1)
# 4
# Create a subplot
ax = fig.add_subplot(224)
# Turn the GeoJSON-ish dict form of the polygon from #1 into a patch
geo = multipolygon.__geo_interface__
patch = PolygonPatch(geo, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
# Fit the figure around the polygon's bounds, render, and save
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
ax.set_aspect(1)
# fig.savefig('patches.png')

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight')
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight')
plt.clf()
