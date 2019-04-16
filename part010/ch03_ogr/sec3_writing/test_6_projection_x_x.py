#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
ds = ogr.Open('/gdata/region_popu.shp')
layer = ds.GetLayer(0)
spatialRef = layer.GetSpatialRef()
print(spatialRef)
...
###############################################################################
from osgeo import osr
wkt = spatialRef.ExportToWkt()
spatial = osr.SpatialReference()
spatial.ImportFromWkt(wkt)
###############################################################################
targetSR = osr.SpatialReference()
targetSR.ImportFromEPSG(4326) #Geo WGS84
###############################################################################
coordTrans = osr.CoordinateTransformation(spatial, targetSR)
###############################################################################
feature = layer.GetFeature(0)
geom = feature.GetGeometryRef()
geom.ExportToWkt()
###############################################################################
geom.Transform(coordTrans)
geom.ExportToWkt()
###############################################################################
targetSR.MorphToESRI()
file = open('/tmp/test.prj', 'w')
file.write(targetSR.ExportToWkt())
file.close()
