# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################
from osgeo import ogr
import os
extfile = 'xx_data_pt.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point', None, ogr.wkbPoint)

################################################################################
fieldcnstr = ogr.FieldDefn("id", ogr.OFTInteger)
layernew.CreateField(fieldcnstr)
fieldf = ogr.FieldDefn("name", ogr.OFTString)
layernew.CreateField(fieldf)

################################################################################
point_coors_arr = [[1, 0], [2, 0], [3, 0], [4, 0]]
for idx, point_coors in enumerate(point_coors_arr):
    wkt = 'POINT (%f %f)' % (point_coors[0], point_coors[1])
    geom = ogr.CreateGeometryFromWkt(wkt)
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetField('id', idx)
    feat.SetField('name', 'ID{0}'.format(idx))
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)

newds.Destroy()

################################################################################
extfile = 'xx_data_line.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point', None, ogr.wkbLineString)
layernew.CreateField(fieldcnstr)
layernew.CreateField(fieldf)

################################################################################
point_coors_arr = [[0, 0, 1, 2, 3, -2, 6, 0]]
for idx, point_coors in enumerate(point_coors_arr):
    wkt = 'LINESTRING (%f %f, %f %f, %f %f, %f %f)' % (
        point_coors[0], point_coors[1], point_coors[2], point_coors[3], point_coors[4], point_coors[5],
        point_coors[6],
        point_coors[7])
    geom = ogr.CreateGeometryFromWkt(wkt)
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetField('id', idx)
    feat.SetField('name', 'line_one')
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)

newds.Destroy()

################################################################################
extfile = 'xx_fig_data_poly.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('polygon', None, ogr.wkbLineString)
layernew.CreateField(fieldcnstr)
layernew.CreateField(fieldf)

################################################################################
wkt_poly_1 = '''POLYGON((2 1, 4 1, 4 3, 12 3, 12 4,6 4,6 6,2 6,2 1))'''
wkt_poly_2 = '''POLYGON((4 1, 8 1, 8 3, 4 3, 4 1))'''
wkt_poly_3 = '''POLYGON((8 4, 10 4, 10 5, 8 5, 8 4))'''
point_coors_arr = [wkt_poly_1, wkt_poly_2, wkt_poly_3]

################################################################################
for idx, point_coors in enumerate(point_coors_arr):
    wkt = point_coors
    geom = ogr.CreateGeometryFromWkt(wkt)
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetField('id', idx)
    feat.SetField('name', 'poly_{idx}'.format(idx=idx))
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)

newds.Destroy()
