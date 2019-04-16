#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point
points = [Point(1,1), Point(2,2), Point(1,0)]
###############################################################################
polygon = Point(1.0, 1.0).buffer(1.0)
from shapely.prepared import prep
prepared_polygon = prep(polygon)
###############################################################################
hits = filter(prepared_polygon.contains, points)
for x in hits:
    print(x.wkt)
