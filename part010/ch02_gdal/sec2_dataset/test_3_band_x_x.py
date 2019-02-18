# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import gdal
rds = gdal.Open('/gdata/lu75c.tif')
rds.RasterCount
band = rds.GetRasterBand(1)

################################################################################
dir(band)

################################################################################
band.XSize
band.YSize
band.DataType

################################################################################
band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()
