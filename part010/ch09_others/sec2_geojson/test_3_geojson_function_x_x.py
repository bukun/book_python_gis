#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import geojson
my_point = geojson.Point((43.24, -1.532))
my_point
###############################################################################
dump = geojson.dumps(my_point, sort_keys=True)
dump
###############################################################################
geojson.loads(dump)
###############################################################################
import geojson
class MyPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def __geo_interface__(self):
        return {'type': 'Point',
                'coordinates': (self.x, self.y)}

point_instance = MyPoint(52.235, -19.234)
geojson.dumps(point_instance, sort_keys=True)
###############################################################################
import geojson
my_line = geojson.LineString([(-152.62, 51.21),
    (5.21, 10.69)])
my_feature = geojson.Feature(geometry=my_line)
list(geojson.utils.coords(my_feature))
###############################################################################
import geojson
new_point = geojson.utils.map_coords(lambda x: x/2,
    geojson.Point((-115.81, 37.24)))
geojson.dumps(new_point, sort_keys=True)
###############################################################################
import geojson
geojson.utils.generate_random("LineString")
