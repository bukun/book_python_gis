# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import mpl_toolkits.basemap
print(mpl_toolkits.basemap.supported_projections)
################################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
bsmap = Basemap(projection='cyl')
bsmap.drawcoastlines()
bsmap.drawmeridians(np.arange(0, 360, 30))
bsmap.drawparallels(np.arange(-90, 90, 30))

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
bsmap = Basemap(projection='aeqd', lon_0=180, lat_0=50)
bsmap.drawmapboundary(fill_color='aqua')
bsmap.fillcontinents(color='coral', lake_color='aqua')
bsmap.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
bsmap = Basemap(projection='mbtfpq', lon_0=105)
bsmap.drawcoastlines()
bsmap.drawmeridians(np.arange(0, 360, 30))
bsmap.drawparallels(np.arange(-90, 90, 30))

# plt.show()

plt.savefig(get_tmp_file(__file__, '3'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '3', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
################################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
bsmap = Basemap(projection='aeqd', lon_0 = 10, lat_0 = 50)
bsmap(10,50)
################################################################################
bsmap(20015077.3712, 20015077.3712, inverse=True)
