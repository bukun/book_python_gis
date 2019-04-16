#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
inshp = '/gdata/GSHHS_c.shp'
from osgeo import ogr
datasource = ogr.Open(inshp)
driver = datasource.GetDriver()
driver.name
###############################################################################
dir(datasource)
###############################################################################
driver = ogr.GetDriverByName('ESRI Shapefile')
###############################################################################
import sys
datasource = driver.Open(inshp,0)
if datasource:
    print('done')
else:
    print('could not open')
###############################################################################
drv_count = ogr.GetDriverCount()
drv_count
###############################################################################
datasource.Destroy()
