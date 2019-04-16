#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
inshp ='/gdata/GSHHS_c.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)
###############################################################################
dir(feature)
###############################################################################
layer.ResetReading()
feature = layer.GetNextFeature()
while feature:
    feature = layer.GetNextFeature()
dir(feature)
###############################################################################
layer.ResetReading()
feat=layer.GetFeature(0)
feat.keys()
feat.GetField('area')
###############################################################################
for i in range(feat.GetFieldCount()):
     print(feat.GetField(i))

###############################################################################
geom = feat.GetGeometryRef()
geom.GetGeometryName()
geom.GetGeometryCount()
geom.GetPointCount()
geom.ExportToWkt()
###############################################################################
arc0=geom.GetGeometryRef(0)
arc0.GetGeometryName()
arc0.GetGeometryCount()
arc0.GetPointCount()
arc0.GetX(0)
arc0.GetY(0)
arc0.GetZ(0)
arc0.ExportToWkt()
