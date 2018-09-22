# -*- coding: utf-8 -*-
'''
在 test_1 中使用的图
'''
from .help_fig_ogr_filter import renderit, create_shp_by_layer


print('=' * 40)
print(__file__)
################################################################################
from osgeo import ogr
import os

shpfile = '/gdata/GSHHS_c.shp'
ds = ogr.Open(shpfile)
layer = ds.GetLayer(0)
lyr_count = layer.GetFeatureCount()
print(lyr_count)
################################################################################
layer.SetAttributeFilter("AREA < 1800000")
lyr_count = layer.GetFeatureCount()
print(lyr_count)
################################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = '/tmp/xx_filter_attr.shp'

create_shp_by_layer(extfile, layer)

#
# if os.access(extfile, os.F_OK):
#     driver.DeleteDataSource(extfile)
# ################################################################################
# newds = driver.CreateDataSource(extfile)
# layernew = newds.CreateLayer('rect', None, ogr.wkbPolygon)
# feat = layer.GetNextFeature()
# while feat is not None:
#     layernew.CreateFeature(feat)
#     feat = layer.GetNextFeature()
# newds.Destroy()

renderit(shpfile=extfile, sig='_attr')
