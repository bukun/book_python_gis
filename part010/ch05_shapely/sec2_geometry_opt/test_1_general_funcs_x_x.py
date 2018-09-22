# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from shapely.geometry import Point
Point(0,0).geom_type
################################################################################
Point(0,0).distance(Point(1,1))
################################################################################
donut = Point(0, 0).buffer(2.0).difference(Point(0, 0).buffer(1.0))
donut.centroid.wkt
donut.representative_point().wkt
################################################################################
from shapely.geometry import Point
point = Point(10, 10)
pt_buf = point.buffer(5)
print(pt_buf.wkt)
