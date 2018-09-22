# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Polygon
from geopandas import GeoSeries
p1 = Polygon([(0, 0), (1, 0), (1, 1)])
p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
g = GeoSeries([p1, p2, p3])
################################################################################
g.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
print (g.area)
################################################################################
buf=g.buffer(0.5)
################################################################################
buf.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
boros = GeoDataFrame.from_file('/gdata/GSHHS_c.shp')
################################################################################
cull = boros['geometry'].convex_hull
cull.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '3'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '3', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
from shapely.geometry import Point
import numpy as np
xmin, xmax, ymin, ymax = -180, 180, -90, 90
xc = (xmax - xmin) * np.random.random(2000) + xmin
yc = (ymax - ymin) * np.random.random(2000) + ymin
pts = GeoSeries([Point(x, y) for x, y in zip(xc, yc)])
################################################################################
circles = pts.buffer(2)
################################################################################
mp = circles.unary_union
################################################################################
holes = boros['geometry'].intersection(mp)
holes.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '4'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '4', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
boros_with_holes = boros['geometry'].difference(mp)
boros_with_holes.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '5'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '5', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
