#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from osgeo import ogr
def create_shp_by_layer(shp, layer):
    outputfile = shp
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver. CreateDataSource ( outputfile )
    pt_layer = newds.CopyLayer ( layer, '')
    newds.Destroy ()
###############################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = '/gdata/GSHHS_h.shp'
world_ds = ogr.Open(world_shp)
world_layer = world_ds.GetLayer(0)
###############################################################################
world_layer.GetFeatureCount()
###############################################################################
cover_shp = '/gdata/spatial_filter.shp'
cover_ds = ogr.Open(cover_shp)
cover_layer = cover_ds.GetLayer(0)
cover_feats = cover_layer.GetNextFeature()
poly = cover_feats.GetGeometryRef()
###############################################################################
world_layer.SetSpatialFilter(poly)
###############################################################################
world_layer.GetFeatureCount()
###############################################################################
out_shp = '/tmp/world_cover.shp'
create_shp_by_layer(out_shp, world_layer)
###############################################################################
world_layer.SetSpatialFilter(None)
world_layer.GetFeatureCount()
###############################################################################
world_layer.SetSpatialFilterRect(-83, 16, -62, 23)
world_layer.GetFeatureCount()
out_shp = '/gdata/world_spatial_filter.shp'
create_shp_by_layer(out_shp, world_layer)
