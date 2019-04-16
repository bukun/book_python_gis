#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['STKaiti']
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
para = {'projection': 'merc',
    'lat_0': 0, 'lon_0': 120,
    'resolution': 'h', 'area_thresh': .1,
    'llcrnrlon': 116,  'llcrnrlat': 36.6,
    'urcrnrlon': 124,  'urcrnrlat': 40.2 }
my_map = Basemap(**para)
my_map.drawcoastlines(); my_map.drawmapboundary()
###############################################################################
lons = [121.60001, 121.38617, 117.19723]
lats = [38.91027, 37.53042, 39.12473]
x, y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)
###############################################################################
labels = ['大连', '烟台', '天津']
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt, ypt, label)
plt.show()
###############################################################################
my_map = Basemap(**para)
my_map.drawcoastlines()
my_map.drawmapboundary()
x,y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt+10000, ypt+5000, label)
plt.show()
