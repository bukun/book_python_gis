#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
inshp='/gdata/GSHHS_c.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
dir(layer)
###############################################################################
layer.GetFeatureCount()
###############################################################################
layer.GetExtent()
###############################################################################
layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(),defn.GetWidth(),defn.GetType(),
        defn.GetPrecision())
