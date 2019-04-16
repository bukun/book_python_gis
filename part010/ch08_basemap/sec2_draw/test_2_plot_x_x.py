#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
para = {'projection': 'merc', 'lat_0': 0, 'lon_0': 120,
    'resolution': 'h', 'area_thresh': .1,
    'llcrnrlon': 116,  'llcrnrlat': 36.6,
    'urcrnrlon': 124,  'urcrnrlat': 40.2 }
my_map = Basemap(**para)
my_map.drawcoastlines(); my_map.drawmapboundary()
###############################################################################
lon =  121.60001; lat = 38.91027
x, y = my_map(lon, lat)
my_map.plot(x, y, 'bo', markersize=12)
plt.show()
###############################################################################
my_map = Basemap(**para)
my_map.drawcoastlines(); my_map.drawmapboundary()
lons = [121.60001, 121.38617, 117.19723]
lats = [38.91027, 37.53042, 39.12473]
x, y = my_map(lons, lats)
###############################################################################
my_map.plot(x, y, 'bo', markersize=10)
plt.show()
###############################################################################
my_map = Basemap(**para)
my_map.drawcoastlines(); my_map.drawmapboundary()
my_map.plot(x, y, marker=None,color='m')
plt.show()
