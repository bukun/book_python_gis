# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from osgeo import gdal
gdal.SetConfigOption('HFA_USE_RRD', 'YES')
################################################################################
dataset = gdal.Open("/gdata/lu75c.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("/tmp/sd2.tif",dataset,0,["INTERLEAVE=PIXEL"])
outDataset = gdal.Open('/tmp/sd2.tif')
outDataset.BuildOverviews(overviewlist=[2,4, 8,16,32,64,128])
