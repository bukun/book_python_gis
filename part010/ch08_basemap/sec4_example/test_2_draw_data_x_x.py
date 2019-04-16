#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
lats, lons, magnitudes = [], [], []
###############################################################################
import csv
filename = '/gdata/all_week.csv'
###############################################################################
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))
        magnitudes.append(float(row[4]))
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
eq_map = Basemap(projection='robin', resolution = 'l',
    area_thresh = 1000.0, lat_0=0, lon_0=-130)
eq_map.drawcoastlines(); eq_map.drawmapboundary()
eq_map.fillcontinents(color = 'gray')
x,y = eq_map(lons, lats)
eq_map.plot(x, y, 'ro', markersize=6)
plt.show()
###############################################################################
eq_map.drawcoastlines(); eq_map.drawmapboundary()
eq_map.fillcontinents(color = 'gray')
min_marker_size = 1.2
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    msize = mag * min_marker_size
    eq_map.plot(x, y, 'ro', markersize=msize)
plt.show()
###############################################################################
def get_marker_color(magnitude):
    if magnitude < 3.0:
        return ('go')
    elif magnitude < 5.0:
        return ('yo')
    else:
        return ('ro')
###############################################################################
eq_map.drawcoastlines(); eq_map.drawmapboundary()
eq_map.fillcontinents(color = 'gray')
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    eq_map.plot(x, y, marker_string, markersize=msize)
plt.show()
