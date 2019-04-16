#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
inshp = '/gdata/region_popu.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
layer.GetSpatialRef()
layer.GetExtent()
###############################################################################
feature = layer.GetFeature(0)
geom = feature.GetGeometryRef()
geom.GetEnvelope()
###############################################################################
sr = geom.GetSpatialReference()
dir(sr)
