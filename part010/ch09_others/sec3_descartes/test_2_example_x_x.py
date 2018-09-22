# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import shapefile as shp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from descartes import PolygonPatch
polys = shp.Reader('/gdata/GSHHS_c.shp')
fig = plt.figure()
ax = fig.gca()
for xx in range(polys.numRecords):
    s = polys.shape(xx)
    poly = s.__geo_interface__
    BLUE = '#6699cc'
    ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2))
ax.axis('scaled')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
