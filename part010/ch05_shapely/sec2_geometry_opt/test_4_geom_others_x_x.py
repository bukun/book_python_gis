# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from shapely.geometry import LineString
line = LineString()
line.is_empty
line.length
line.bounds
line.coords
################################################################################
line.coords = [(0, 0), (1, 1)]
line.is_empty
line.length
line.bounds
################################################################################
ip = LineString([(0, 0), (0, 1), (1, 1)]).interpolate(1.5)
ip.wkt
LineString([(0, 0), (0, 1), (1, 1)]).interpolate(0.75, normalized=True).wkt
################################################################################
LineString([(0, 0), (0, 1), (1, 1)]).project(ip)
LineString([(0, 0), (0, 1), (1, 1)]).project(ip, normalized=True)
################################################################################
