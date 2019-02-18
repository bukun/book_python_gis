# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
para = {
    'projection': 'merc', 'lat_0': 0, 'lon_0': 120,
    'resolution': 'l', 'area_thresh': 1000.0,
    'llcrnrlon': 116, 'llcrnrlat': 36.6,
    'urcrnrlon': 124, 'urcrnrlat': 40.2 }

################################################################################

my_map = Basemap(**para)
my_map.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()

################################################################################
para['resolution'] = 'h'
my_map = Basemap(**para)
my_map.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()

################################################################################
para['area_thresh'] = .1
my_map = Basemap(**para)
my_map.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '3'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '3', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
