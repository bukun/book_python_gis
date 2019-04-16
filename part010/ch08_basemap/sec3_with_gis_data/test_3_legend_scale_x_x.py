#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
p1 = plt.subplot(121)
para = {'projection': 'tmerc','lat_0': 0,'lon_0': 3,
    'llcrnrlon': 1.819757266426611,
    'llcrnrlat': 41.583851612359275,
    'urcrnrlon': 1.841589961763497,
    'urcrnrlat': 41.598674173123 }
dem_tif = '/gdata/sample_files/dem.tiff'
mymap = Basemap(**para)
from osgeo import gdal
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
from numpy import linspace
from numpy import meshgrid
x = linspace(0, mymap.urcrnrx, data.shape[1])
y = linspace(0, mymap.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
mymap.contourf(xx, yy, data)
###############################################################################
p2 = plt.subplot(122)
mymap = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, mymap.urcrnrx, data.shape[1])
y = linspace(0, mymap.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
mymap.pcolor(xx, yy, data)
plt.show()
###############################################################################
mymap = Basemap(**para)
ds = gdal.Open("/gdata/sample_files/dem.tiff")
data = ds.ReadAsArray()
x = linspace(0, mymap.urcrnrx, data.shape[1])
y = linspace(0, mymap.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
###############################################################################
cmap = plt.get_cmap('PiYG')
colormesh = mymap.pcolormesh(xx, yy, data, vmin = 500,
    vmax = 1300, cmap=cmap)
ctr = mymap.contour(xx, yy, data, range(500, 1350, 50),
    colors = 'k', linestyles = 'solid')
mymap.colorbar(colormesh)
###############################################################################
cb = mymap.colorbar(mappable=colormesh, location='bottom',
    label="等高线")
cb.add_lines(ctr)
cb.set_ticks([600, 760, 1030, 1210])
plt.show()
