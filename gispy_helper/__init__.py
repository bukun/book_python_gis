# -*- coding: utf-8 -*-

from osgeo import ogr
import os
import time

# from helper.textool import get_tmp_file
import canvasvg
import cairosvg

import turtle

BASE_PATH = '/gdata/fig_data'
if os.path.exists(BASE_PATH):
    pass
else:
    os.makedirs(BASE_PATH)

import os, mapnik


def mapnik_lyr(mapobj, data=None, line_sym=None):
    ################################################################################
    # m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")
    s = mapnik.Style()
    r = mapnik.Rule()
    r.symbols.append(line_sym)
    s.rules.append(r)
    sname = str(int(time.time()))
    print(sname)
    time.sleep(1)
    mapobj.append_style(sname, s)

    # line_symbolizer = mapnik.LineSymbolizer()
    # line_symbolizer.stroke = mapnik.Color('rgb(100%,50%,50%)')
    # ################################################################################
    # line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
    #
    # line_symbolizer.stroke_width = 4.0
    #
    # s2 = mapnik.Style()
    # r2 = mapnik.Rule()
    # r2.symbols.append(line_symbolizer)
    # s2.rules.append(r2)
    # mapobj.append_style('My Style2', s2)

    lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
    # lyr.datasource = mapnik.Shapefile(file='/gdata/world_borders.shp')
    lyr.datasource = mapnik.Shapefile(file=data)
    lyr.styles.append(sname)

    return lyr


def renderit(line_sym=None, poly_sym=None, point_sym=None, shpfile=None, fig_index=0):
    ################################################################################
    m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")
    s = mapnik.Style()
    r = mapnik.Rule()
    # line_sym.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
    # line_sym.stroke_linejoin = mapnik.stroke_linejoin.ROUND_JOIN
    # line_sym.stroke_dasharray = [(3,4)]
    # line_sym.stroke_linecap = mapnik.stroke_linecap.SQUARE_CAP

    if poly_sym:
        r.symbols.append(poly_sym)
    if point_sym:
        r.symbols.append(point_sym)
    if line_sym:
        r.symbols.append(line_sym)
    s.rules.append(r)
    m.append_style('My Style', s)
    lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
    # lyr.datasource = mapnik.Shapefile(file='/gdata/world_borders.shp')
    if shpfile:
        lyr.datasource = mapnik.Shapefile(file=shpfile)
    else:
        lyr.datasource = mapnik.Shapefile(file=os.path.join(BASE_PATH, 'fig_data_line.shp'))
    lyr.styles.append('My Style')
    m.layers.append(lyr)
    # bbox = mapnik.Box2d(118, 36.6, 124.6, 40.7)
    # m.zoom_to_box(bbox)
    m.zoom_all()
    return m


# -*- coding: utf-8 -*-
import os


# import config
#
# os.chdir(config.gisws)

# from helper.textool import get_tmp_file


def gen_poly():
    extfile = os.path.join(BASE_PATH, 'fig_data_poly.shp')  # get_tmp_file(__file__, '_line', 'shp')
    driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.access(extfile, os.F_OK):
        driver.DeleteDataSource(extfile)
    newds = driver.CreateDataSource(extfile)
    layernew = newds.CreateLayer('polygon', None, ogr.wkbPolygon)

    fieldcnstr = ogr.FieldDefn("id", ogr.OFTInteger)
    # fieldcnstr.SetWidth(32)
    layernew.CreateField(fieldcnstr)
    fieldf = ogr.FieldDefn("name", ogr.OFTString)
    layernew.CreateField(fieldf)

    wkt_poly_1 = '''POLYGON((2 1, 4 1, 4 3, 12 3, 12 4,6 4,6 6,2 6,2 1))'''
    wkt_poly_2 = '''POLYGON((4 1, 8 1, 8 3, 4 3, 4 1))'''
    wkt_poly_3 = '''POLYGON((8 4, 10 4, 10 5, 8 5, 8 4))'''

    wkt_poly_1 = '''POLYGON((3 1, 6 1, 6 3, 18 3, 18 4,9 4,9 6,3 6,3 1))'''
    wkt_poly_2 = '''POLYGON((6 1, 12 1, 12 3, 6 3, 6 1))'''
    wkt_poly_3 = '''POLYGON((12 4, 15 4, 15 5, 12 5, 12 4))'''

    point_coors_arr = [wkt_poly_1, wkt_poly_2, wkt_poly_3]

    idx = 1
    for point_coors in point_coors_arr:
        wkt = point_coors
        # wkt = 'LINESTRING(3 4,10 50,20 25)'
        print(wkt)
        geom = ogr.CreateGeometryFromWkt(wkt)
        feat = ogr.Feature(layernew.GetLayerDefn())
        feat.SetField('id', idx)
        feat.SetField('name', 'poly_{idx}'.format(idx=idx))
        feat.SetGeometry(geom)
        layernew.CreateFeature(feat)
        idx += 1
    newds.Destroy()


# 创建线状数据集


def gen_line():
    extfile = os.path.join(BASE_PATH, 'fig_data_line.shp')  # get_tmp_file(__file__, '_line', 'shp')
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

    point_coors_arr = [[0, 0, 1, 2, 3, -2, 6, 0]]
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
        feat.SetField('name', 'line_one')
        feat.SetGeometry(geom)
        layernew.CreateFeature(feat)
        idx += 1
    newds.Destroy()


def gen_line3():
    extfile = os.path.join(BASE_PATH, 'fig_data_line3.shp')  # get_tmp_file(__file__, '_line', 'shp')
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
        feat.SetField('name', 'line_one')
        feat.SetGeometry(geom)
        layernew.CreateFeature(feat)
        idx += 1
    newds.Destroy()


def gen_label():
    extfile = os.path.join(BASE_PATH, 'fig_data_pt.shp')
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

    point_coors_arr = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]

    idx = 1
    for point_coors in point_coors_arr:
        wkt = 'POINT (%f %f)' % (point_coors[0], point_coors[1])
        # wkt = 'LINESTRING(3 4,10 50,20 25)'
        print(wkt)
        geom = ogr.CreateGeometryFromWkt(wkt)
        feat = ogr.Feature(layernew.GetLayerDefn())
        feat.SetField('id', idx)
        feat.SetField('name', 'Label')
        feat.SetGeometry(geom)
        layernew.CreateFeature(feat)
        idx += 1
    newds.Destroy()


def gen_turtle():
    result_png = os.path.join(BASE_PATH, 'turtle.png')
    if os.path.exists(result_png):
        return True
    turtle.ht()
    turtle.color("purple")
    turtle.pensize(2)
    turtle.goto(4, 8)
    turtle.goto(8, 0)
    turtle.goto(0, 0)

    ts = turtle.getscreen()

    ts = turtle.getscreen().getcanvas()

    tmpfile = 'xx_tmp.svg'

    canvasvg.saveall(tmpfile, ts)
    with open(tmpfile) as svg_input, open(result_png, 'wb') as png_output:
        cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)


# canvasvg.saveall(get_tmp_file(__file__, 't', file_ext='svg'), ts)

gen_turtle()
gen_label()
gen_line3()
gen_line()
gen_poly()
