# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from shapely.geometry import Point
from shapely.prepared import prep
points = [Point(1,1), Point(2,2)] # large list
from shapely.geometry import Point
polygon = Point(0.0, 0.0).buffer(1.0)
prepared_polygon = prep(polygon)
prepared_polygon
hits = filter(prepared_polygon.contains, points)
hits
