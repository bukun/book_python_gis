# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.subplot(121)
bsmap = Basemap(projection='ortho',lon_0=0,lat_0=0,resolution='c')
bsmap.drawmapboundary()
plt.subplot(122)
bsmap = Basemap(projection='sinu',lon_0=0,resolution='c')
bsmap.drawmapboundary(fill_color='aqua')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
################################################################################
bsmap = Basemap()
bsmap.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
bsmap = Basemap(projection='poly',
              lon_0=0.0, lat_0=0,
              llcrnrlon=-80.,llcrnrlat=-40,urcrnrlon=80.,urcrnrlat=40.)
bsmap.drawmapboundary(fill_color='aqua')
bsmap.fillcontinents(color='coral',lake_color='aqua')
bsmap.drawcoastlines()
################################################################################
bsmap.drawmeridians(range(0, 360, 20))
################################################################################
bsmap.drawparallels(range(-90, 100, 10), linewidth=2, dashes=[4, 2],
   labels=[1,0,0,1], color='r' )

# plt.show()

plt.savefig(get_tmp_file(__file__, '3'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '3', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
################################################################################
################################################################################
################################################################################
bsmap = Basemap(projection='ortho', lat_0=0, lon_0=0)
bsmap.drawmapboundary(fill_color='aqua')
################################################################################
bsmap.fillcontinents(color='coral',lake_color='aqua')
bsmap.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '4'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '4', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
################################################################################
import matplotlib
matplotlib.use('Agg')
