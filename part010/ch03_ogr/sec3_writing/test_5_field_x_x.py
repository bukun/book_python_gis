#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from osgeo import ogr
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = '/tmp/rect3.shp'
if os.access( extfile, os.F_OK ):
    driver.DeleteDataSource( extfile )
###############################################################################
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect3',None,ogr.wkbPolygon)
###############################################################################
field_name = ogr.FieldDefn("name",ogr.OFTString)
field_name.SetWidth(36)
field_area = ogr.FieldDefn("area",ogr.OFTReal)
###############################################################################
layernew.CreateField(field_name)
layernew.CreateField(field_area)
###############################################################################
laydef = layernew.GetLayerDefn()
laydef.GetFieldCount()
###############################################################################
newds.Destroy()
