# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################

################################################################################
import mapnik
m = mapnik.Map(600, 400, "+proj=latlong +datum=WGS84")
lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='/gdata/GSHHS_c.shp')
lyr.styles.append('My Style')
m.layers.append(lyr)
m.scale_denominator(), m.scale()

################################################################################
bbox = mapnik.Box2d(70, 20, 135, 57)
m.zoom_to_box(bbox)
m.scale_denominator(), m.scale()
