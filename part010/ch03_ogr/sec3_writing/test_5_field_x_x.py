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
fieldcnstr = ogr.FieldDefn("类型",ogr.OFTString)
fieldcnstr.SetWidth(36)
fieldf = ogr.FieldDefn("area",ogr.OFTReal)
###############################################################################
laydef = layernew.GetLayerDefn()
laydef.AddFieldDefn(fieldcnstr)
laydef.AddFieldDefn(fieldf)
laydef.GetFieldCount()
###############################################################################
newds.Destroy()
