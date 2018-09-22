# -*- coding: utf-8 -*-
'''
这个文件，辅助用来生成图。
'''
# 创建多边形数据集
from osgeo import ogr
import os, math
from .help_fig_ogr_filter import renderit, create_shp_by_layer

driver = ogr.GetDriverByName("ESRI Shapefile")

# extfile = 'gdata/xx_demo_poly.shp'
poly_filter = '/tmp/xx_poly_filter.shp'

if os.access(poly_filter, os.F_OK):
    driver.DeleteDataSource(poly_filter)

# 西、东、南、北
extent = [-83, -62, 16, 23]

newds = driver.CreateDataSource(poly_filter)
layernew = newds.CreateLayer('rect', None, ogr.wkbPolygon)
width = math.fabs(extent[1] - extent[0])
height = math.fabs(extent[3] - extent[3])
tw = width / 2
th = width / 2
extnew = extent[0] + tw
wkt = 'POLYGON ((%f %f, %f %f, %f %f, %f %f, %f %f ))' % (
    extent[0], extent[3], extent[1], extent[3], extent[1], extent[2], extent[0], extent[2], extent[0], extent[3])

geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

################################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = '/gdata/GSHHS_h.shp'
cover_shp = '/tmp/xx_poly_filter.shp'
world_ds = ogr.Open(world_shp)
cover_ds = ogr.Open(cover_shp)
world_layer = world_ds.GetLayer(0)
cover_layer = cover_ds.GetLayer(0)
################################################################################
world_layer.GetFeatureCount()
# 使用多边形要素进行选择
################################################################################
cover_feats = cover_layer.GetNextFeature()
poly = cover_feats.GetGeometryRef()
world_layer.SetSpatialFilter(poly)
out_shp = '/tmp/world_cover.shp'
create_shp_by_layer(out_shp, world_layer)
################################################################################

# 下面是使用多边形参数选择
shpfile = '/gdata/GSHHS_h.shp'
ds = ogr.Open(shpfile)
world_layer = ds.GetLayer(0)
#  minx, double miny, double maxx, double maxy
world_layer.SetSpatialFilterRect(-83, 16, -62, 23)
print(world_layer.GetFeatureCount())
################################################################################
out_shp_rec = '/tmp/xx_world_spatial_filter.shp'
create_shp_by_layer(out_shp_rec, world_layer)

################################################################################

renderit(shpfile=out_shp, sig='_spatial_a')
renderit(shpfile=out_shp_rec, sig='_spatial_b')
