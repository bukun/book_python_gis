#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import LineString
line = LineString([(0, 0), (1, 1)])
line.area
line.length
###############################################################################
line.bounds
###############################################################################
len(line.coords)
list(line.coords)
line.coords[1:]
###############################################################################
LineString(line)
###############################################################################
from shapely.geometry import LinearRing
ring = LinearRing([(0, 0), (1, 1), (1, 0)])
list(ring.coords)
###############################################################################
from shapely.geometry import Polygon
polygon = Polygon([(0, 0), (1, 1), (1, 0)])
###############################################################################
list(polygon.interiors)
###############################################################################
coords = [(0, 0), (1, 1), (1, 0)]
r = LinearRing(coords)
s = Polygon(r)
s.area
###############################################################################
t = Polygon(s.buffer(1.0).exterior, [r])
t.area
###############################################################################
from shapely.geometry import box
b = box(0.0, 0.0, 1.0, 1.0)
list(b.exterior.coords)
###############################################################################
line = LineString()
line.is_empty
line.length
line.bounds
line.coords
###############################################################################
line.coords = [(0, 0), (1, 1)]
line.is_empty
line.length
line.bounds
