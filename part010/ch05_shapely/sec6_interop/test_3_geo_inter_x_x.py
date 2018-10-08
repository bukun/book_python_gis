# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from shapely.geometry import asShape
d = {"type": "Point", "coordinates": (0.0, 0.0)}
shape = asShape(d)
shape.geom_type
tuple(shape.coords)
list(shape.coords)
################################################################################
class GeoThing(object):
    def __init__(self, d):
        self.__geo_interface__ = d
################################################################################
thing = GeoThing(d)
shape = asShape(thing)
shape.geom_type
tuple(shape.coords)
list(shape.coords)
################################################################################
from shapely.geometry import mapping
thing = GeoThing(d)
m = mapping(thing)
type(m)
m['type']
