# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from osgeo import gdalconst
dir(gdalconst)
################################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/geotiff_file.tif")
band = dataset.GetRasterBand(1)
band.DataType
