# -*- coding: utf-8 -*-
import os
# import config
#
# os.chdir(config.gisws)

from helper.textool import get_tmp_file

# 创建线状数据集
from osgeo import ogr
import os


def gen_line():
    extfile = get_tmp_file(__file__, '_line', 'shp')
    driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.access(extfile, os.F_OK):
        driver.DeleteDataSource(extfile)
    newds = driver.CreateDataSource(extfile)
    layernew = newds.CreateLayer('point', None, ogr.wkbLineString)

    fieldcnstr = ogr.FieldDefn("id", ogr.OFTInteger)
    # fieldcnstr.SetWidth(32)
    layernew.CreateField(fieldcnstr)
    fieldf = ogr.FieldDefn("name", ogr.OFTString)
    layernew.CreateField(fieldf)

    point_coors_arr = [
        [0, 0, 1, 2, 3, -2, 6, 0],
        [7, 0, 8, 2, 10, -2, 13, 0],
        [14, 0, 15, 2, 17, -2, 20, 0]]
    idx = 1
    for point_coors in point_coors_arr:
        wkt = 'LINESTRING (%f %f, %f %f, %f %f, %f %f)' % (
            point_coors[0], point_coors[1], point_coors[2], point_coors[3], point_coors[4], point_coors[5],
            point_coors[6],
            point_coors[7])
        # wkt = 'LINESTRING(3 4,10 50,20 25)'
        print(wkt)
        geom = ogr.CreateGeometryFromWkt(wkt)
        feat = ogr.Feature(layernew.GetLayerDefn())
        feat.SetField('id', idx)
        feat.SetField('name', 'road')
        feat.SetGeometry(geom)
        layernew.CreateFeature(feat)
        idx += 1
    newds.Destroy()


def gen_label():
    extfile = get_tmp_file(__file__, '_pt', 'shp')
    driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.access(extfile, os.F_OK):
        driver.DeleteDataSource(extfile)
    newds = driver.CreateDataSource(extfile)
    layernew = newds.CreateLayer('point', None, ogr.wkbPoint)

    fieldcnstr = ogr.FieldDefn("id", ogr.OFTInteger)
    # fieldcnstr.SetWidth(32)
    layernew.CreateField(fieldcnstr)
    fieldf = ogr.FieldDefn("name", ogr.OFTString)
    layernew.CreateField(fieldf)

    point_coors_arr = [
        [1, 0],
        [2, 0],
        [3, 0],
        [4, 0],
    ]

    idx = 1
    for point_coors in point_coors_arr:
        wkt = 'POINT (%f %f)' % (point_coors[0], point_coors[1])
        # wkt = 'LINESTRING(3 4,10 50,20 25)'
        print(wkt)
        geom = ogr.CreateGeometryFromWkt(wkt)
        feat = ogr.Feature(layernew.GetLayerDefn())
        feat.SetField('id', idx)
        feat.SetField('name', '标注')
        feat.SetGeometry(geom)
        layernew.CreateFeature(feat)
        idx += 1
    newds.Destroy()

gen_label()
gen_line()
