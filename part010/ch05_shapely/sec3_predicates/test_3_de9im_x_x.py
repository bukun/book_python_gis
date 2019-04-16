#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point
Point(0, 0).relate(Point(1, 1))
###############################################################################
from shapely.geometry import LineString
Point(0, 0).relate(LineString([(0, 0), (1, 1)]))
