# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
################################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/lu75c.tif")
from numpy import *
dataset.ReadAsArray(2500,2500,3,3)
array([[12, 12, 12],
[12, 12, 12],
[12, 12, 12]],dtype=int16)
dataset.ReadRaster(2500,2500,3,3)
