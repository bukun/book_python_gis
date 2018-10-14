# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from shapely.geometry import MultiLineString
coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)
lines.boundary.wkt
lines.boundary.boundary.wkt
lines.boundary.boundary.is_empty

################################################################################
from shapely.geometry import LineString
LineString([(0, 0), (1, 1)]).centroid.wkt

################################################################################
from shapely.geometry import Point
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.difference(b).wkt

################################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.intersection(b).wkt

################################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.symmetric_difference(b).wkt

################################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.union(b).wkt

################################################################################
a.union(b).boundary.wkt
a.boundary.union(b.boundary).wkt
