# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from shapely.geometry import Point
from shapely.ops import cascaded_union
polygons = [Point(i, 0).buffer(0.7) for i in range(5)]
################################################################################
cascaded_union(polygons)
################################################################################
from shapely.geometry import MultiPolygon
m = MultiPolygon(polygons)
m.area
cascaded_union(m).area
