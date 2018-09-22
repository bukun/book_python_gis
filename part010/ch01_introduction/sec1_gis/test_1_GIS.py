# # -*- coding: utf-8 -*-
#
# ###################################################################################
# # 创建点状数据集
# ####################################################################################
#
# import os
# from osgeo import ogr
#
# # 结果数据
# extfile = os.path.join(os.path.dirname(__file__), 'xx_demo_point.shp')
# point_coors = [[300, 450], [750, 700], [1200, 450], [750, 200], [750, 450]]
# driver = ogr.GetDriverByName("ESRI Shapefile")
# if os.access(extfile, os.F_OK):
#     driver.DeleteDataSource(extfile)
# newds = driver.CreateDataSource(extfile)
# layernew = newds.CreateLayer('point', None, ogr.wkbPoint)
# # 创建字段
# fieldf_x = ogr.FieldDefn("x", ogr.OFTReal)
# fieldf_y = ogr.FieldDefn("y", ogr.OFTReal)
# layernew.CreateField(fieldf_x)
# layernew.CreateField(fieldf_y)
# # 创建点
# for aa in point_coors:
#     geom = ogr.CreateGeometryFromWkt('POINT ({0} {1})'.format(aa[0], aa[1]))
#     feat = ogr.Feature(layernew.GetLayerDefn())
#     feat.SetField('x', aa[0])
#     feat.SetField('y', aa[1])
#     feat.SetGeometry(geom)
#     layernew.CreateFeature(feat)
# newds.Destroy()
#
# #######################################################
# # 创建线状数据集
# #######################################################
# from osgeo import ogr
# import os, math
#
# driver = ogr.GetDriverByName("ESRI Shapefile")
#
# # extfile = 'gdata/xx_demo_line.shp'
# extfile = os.path.join(os.path.dirname(__file__), 'xx_demo_line.shp')
# point_coors = [300, 450, 750, 700, 1200, 450, 750, 200]
# print(point_coors)
# if os.access(extfile, os.F_OK):
#     driver.DeleteDataSource(extfile)
#
# newds2 = driver.CreateDataSource(extfile)
# layernew2 = newds2.CreateLayer('point', None, ogr.wkbLineString)
#
# wkt = 'LINESTRING (%f %f, %f %f, %f %f, %f %f, %f %f)' % (
#     point_coors[0], point_coors[1], point_coors[2], point_coors[3], point_coors[4], point_coors[5], point_coors[6],
#     point_coors[7], point_coors[0], point_coors[1])
#
# print('Line string: {0}'.format(wkt))
# geom = ogr.CreateGeometryFromWkt(wkt)
# feat = ogr.Feature(layernew2.GetLayerDefn())
# feat.SetGeometry(geom)
# layernew2.CreateFeature(feat)
# newds2.Destroy()
#
# # 创建多边形数据集
# from osgeo import ogr
# import os, math
#
# driver = ogr.GetDriverByName("ESRI Shapefile")
#
# # extfile = 'gdata/xx_demo_poly.shp'
# extfile = os.path.join(os.path.dirname(__file__), 'xx_demo_poly.shp')
#
# if os.access(extfile, os.F_OK):
#     driver.DeleteDataSource(extfile)
#
# extent = [400, 1100, 300, 600]
#
# newds = driver.CreateDataSource(extfile)
# layernew = newds.CreateLayer('rect', None, ogr.wkbPolygon)
# width = math.fabs(extent[1] - extent[0])
# height = math.fabs(extent[3] - extent[3])
# tw = width / 2
# th = width / 2
# extnew = extent[0] + tw
# wkt = 'POLYGON ((%f %f, %f %f, %f %f, %f %f, %f %f ))' % (
#     extent[0], extent[3], extent[1], extent[3], extent[1], extent[2], extent[0], extent[2], extent[0], extent[3])
#
# geom = ogr.CreateGeometryFromWkt(wkt)
# feat = ogr.Feature(layernew.GetLayerDefn())
# feat.SetGeometry(geom)
# layernew.CreateFeature(feat)
# newds.Destroy()