#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point
from numpy import array
array(Point(0, 0))
from shapely.geometry import LineString
array(LineString([(0, 0), (1, 1)]))
###############################################################################
Point(0, 0).xy
LineString([(0, 0), (1, 1)]).xy
###############################################################################
from shapely.geometry import asPoint
pa = asPoint(array([0.0, 0.0]))
pa.wkt
###############################################################################
from shapely.geometry import asLineString
la = asLineString(array([[1.0, 2.0], [3.0, 4.0]]))
la.wkt
