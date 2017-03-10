import shapefile as shp
import matplotlib.pyplot as plt

from descartes import PolygonPatch


# sf = shp.Reader('gdata/world_borders.shp')


polys  = shp.Reader('gdata/world_borders.shp')
# first polygon
fig = plt.figure()
ax = fig.gca()


for xx in range(polys.numRecords):
    s = polys.shape(xx)
    poly = s.__geo_interface__


    BLUE = '#6699cc'


    ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))

ax.axis('scaled')
plt.show()