#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
gdal.SetConfigOption('HFA_USE_RRD', 'YES')
###############################################################################
rds = gdal.Open("/gdata/lu75c.tif")
rds.BuildOverviews(overviewlist=[2,4, 8,16,32,64,128])
