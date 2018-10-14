# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import ogr
inshp = '/gdata/county_popu.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
layer.GetSpatialRef()
layer.GetExtent()

################################################################################
feature = layer.GetFeature(0)
geom = feature.GetGeometryRef()
geom.GetEnvelope()

################################################################################
geom.GetSpatialReference()
dir(geom)
