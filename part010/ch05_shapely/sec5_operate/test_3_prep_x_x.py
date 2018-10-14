# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from shapely.geometry import Point
points = [Point(1,1), Point(2,2), Point(1,0)]

################################################################################
polygon = Point(1.0, 1.0).buffer(1.0)
from shapely.prepared import prep
prepared_polygon = prep(polygon)

################################################################################
hits = filter(prepared_polygon.contains, points)
for x in hits:
    print(x.wkt)
