#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/geotiff_file.tif")
dataset.GetGCPs()
gtrans = dataset.GetGeoTransform()
gtrans
###############################################################################
dataset.RasterXSize
dataset.RasterYSize
###############################################################################
