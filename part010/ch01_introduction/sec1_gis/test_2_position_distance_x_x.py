# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import os
from osgeo import ogr
extfile = 'xx_demo_point.shp'
################################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point', None, ogr.wkbPoint)
################################################################################
fieldf_x = ogr.FieldDefn("x", ogr.OFTReal)
fieldf_y = ogr.FieldDefn("y", ogr.OFTReal)
layernew.CreateField(fieldf_x)
layernew.CreateField(fieldf_y)
################################################################################
point_coors = [[300, 450], [750, 700], [1200, 450], [750, 200], [750, 450]]
for pt in point_coors:
    geom = ogr.CreateGeometryFromWkt('POINT ({0} {1})'.format(pt[0], pt[1]))
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetField('x', pt[0])
    feat.SetField('y', pt[1])
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)
newds.Destroy()
