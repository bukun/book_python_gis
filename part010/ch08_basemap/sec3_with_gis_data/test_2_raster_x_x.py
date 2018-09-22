# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from osgeo import gdal
from numpy import linspace
from numpy import meshgrid
para = {
    'projection': 'tmerc',
    'lat_0': 0,
    'lon_0': 3,
    'llcrnrlon': 1.819757266426611,
    'llcrnrlat': 41.583851612359275,
    'urcrnrlon': 1.841589961763497,
    'urcrnrlat': 41.598674173123 }
dem_tif = '/gdata/sample_files/dem.tiff'
################################################################################
p1 = plt.subplot(121)
mymap = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, mymap.urcrnrx, data.shape[1])
y = linspace(0, mymap.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
cs = mymap.contour(xx, yy, data, range(400, 1500, 100), cmap=plt.cm.cubehelix)
################################################################################
p2 = plt.subplot(122)
mymap = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, mymap.urcrnrx, data.shape[1])
y = linspace(0, mymap.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
cs = mymap.contour(xx, yy, data, range(400, 1500, 100), cmap=plt.cm.cubehelix)
plt.clabel(cs, inline=True, fmt='%1.0f', fontsize=8, colors='k')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
