#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
para = {
    'projection': 'merc', 'lat_0': 0, 'lon_0': 120,
    'resolution': 'l', 'area_thresh': 1000.0,
    'llcrnrlon': 116, 'llcrnrlat': 36.6,
    'urcrnrlon': 124, 'urcrnrlat': 40.2 }
###############################################################################
my_map = Basemap(**para)
my_map.drawcoastlines()
plt.show()
###############################################################################
para['resolution'] = 'h'
my_map = Basemap(**para)
my_map.drawcoastlines()
plt.show()
###############################################################################
para['area_thresh'] = .1
my_map = Basemap(**para)
my_map.drawcoastlines()
plt.show()
