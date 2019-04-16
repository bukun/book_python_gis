#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point
Point(0, 0).has_z
Point(0, 0, 0).has_z
###############################################################################
from shapely.geometry import LinearRing
LinearRing([(1,0), (1,1), (0,0)]).is_ccw
###############################################################################
ring = LinearRing([(0,0), (1,1), (1,0)])
ring.is_ccw
ring.coords = list(ring.coords)[::-1]
ring.is_ccw
###############################################################################
from shapely.geometry import Point
Point().is_empty
Point(0, 0).is_empty
###############################################################################
from operator import attrgetter
empties = filter(attrgetter('is_empty'),
    [Point(), Point(0, 0)])
for g in empties: print(g.wkt)

###############################################################################
from shapely.geometry import LineString
LineString([(0, 0), (1, 1), (1, -1)]).is_ring
from shapely.geometry import LinearRing
LinearRing([(0, 0), (1, 1), (1, -1)]).is_ring
###############################################################################
LineString([(0, 0),(1, 1),(1, -1),(0, 1)]).is_simple
###############################################################################
from shapely.geometry import MultiPolygon
poly = MultiPolygon([Point(0, 0).buffer(2.0),
    Point(1, 1).buffer(2.0)])
poly.is_valid
###############################################################################
from shapely.validation import explain_validity
explain_validity(poly)
