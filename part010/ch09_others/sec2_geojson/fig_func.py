import shapefile as shp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from descartes import PolygonPatch



import geojson

uu = geojson.Polygon([
    [(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)],
    [(-5.21, 23.51), (15.21, -10.81), (-20.51, 1.51), (-5.21, 23.51)]
])


point_instance = uu.__geo_interface__

fig = plt.figure()
ax = fig.gca()
# for xx in range(polys.numRecords):
#     s = polys.shape(xx)
    # poly = s.__geo_interface__
BLUE = '#6699cc'

ax.add_patch(PolygonPatch(point_instance, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2))
ax.axis('scaled')

# plt.show()

plt.savefig('uu.png')
plt.clf()