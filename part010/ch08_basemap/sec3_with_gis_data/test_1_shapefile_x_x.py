#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
para = {'projection': 'tmerc', 'lat_0': 35, 'lon_0': -5,
    'resolution': 'i', 'llcrnrlon': -30, 'llcrnrlat': 45,
    'urcrnrlon': 20,  'urcrnrlat': 25 }
mymap = Basemap(**para)
###############################################################################
mymap.readshapefile('/gdata/GSHHS_h', 'comarques')
plt.show()
