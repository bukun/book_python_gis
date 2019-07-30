#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
from gdalconst import *
dataset = gdal.Open("/gdata/geotiff_file.tif")
band = dataset.GetRasterBand(1)
band.ReadAsArray(100,100,5,5,10,10)
###############################################################################
band.XSize
band.YSize
band.ReadAsArray(1496,896,5,5)
