# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
mymap = Basemap(llcrnrlon=-25,llcrnrlat=30,urcrnrlon=25.,urcrnrlat=50,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)
################################################################################
mymap.readshapefile('/gdata/GSHHS_h', 'comarques')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
import matplotlib
matplotlib.use('Agg')
################################################################################
mymap.readshapefile('/gdata/GSHHS_h', 'comarques')
mymap.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')
mymap.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize = 14)

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
