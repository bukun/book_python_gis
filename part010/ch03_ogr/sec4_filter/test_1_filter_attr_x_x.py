#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
import os
shpfile = '/gdata/GSHHS_h.shp'
ds = ogr.Open(shpfile)
layer = ds.GetLayer(0)
layer.GetFeatureCount()
###############################################################################
layer.SetAttributeFilter("AREA < 1800000")
lyr_count = layer.GetFeatureCount()
print(lyr_count)
###############################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = '/tmp/xx_filter_attr.shp'
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
lyrn = newds.CreateLayer('rect', None, ogr.wkbPolygon)
feat = layer.GetNextFeature()
while feat is not None:
    lyrn.CreateFeature(feat)
    feat = layer.GetNextFeature()
newds.Destroy()
