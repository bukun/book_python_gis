#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdalconst
dir(gdalconst)
###############################################################################
from osgeo import gdal
rds = gdal.Open("/gdata/geotiff_file.tif")
band = rds.GetRasterBand(1)
band.DataType
