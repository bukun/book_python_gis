# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from shapely.geometry import Point
Point(0, 0).relate(Point(1, 1))

################################################################################
from shapely.geometry import LineString
Point(0, 0).relate(LineString([(0, 0), (1, 1)]))
