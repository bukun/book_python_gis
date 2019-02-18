# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
para = {'projection': 'tmerc', 'lat_0': 35, 'lon_0': -5,
    'resolution': 'i', 'llcrnrlon': -30, 'llcrnrlat': 45,
    'urcrnrlon': 20,  'urcrnrlat': 25 }

mymap = Basemap(**para)

################################################################################
mymap.readshapefile('/gdata/GSHHS_h', 'comarques')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
