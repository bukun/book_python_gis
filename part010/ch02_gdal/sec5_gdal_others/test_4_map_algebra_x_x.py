# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import gdal
import numpy
dataset = gdal.Open("/gdata/geotiff_file.tif")
band2 = dataset.GetRasterBand(2)
band3 = dataset.GetRasterBand(3)
cols = 100
rows = 100
data2 = band2.ReadAsArray(0, 0,
    cols,rows).astype(numpy.float16)

data3 = band3.ReadAsArray(0, 0,
    cols,rows).astype(numpy.float16)

################################################################################

mask = numpy.greater(data3 + data2, 0)

################################################################################
ndvi = numpy.choose(mask,
    (-99, (data3 - data2) / (data3 + data2)))

ndvi
