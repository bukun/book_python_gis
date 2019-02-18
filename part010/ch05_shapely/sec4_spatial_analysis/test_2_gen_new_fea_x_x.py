# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from shapely.geometry import LineString
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2),
    (3, 1), (1, 0)])

dilated = line.buffer(0.5)
eroded = dilated.buffer(-0.3)

################################################################################
from shapely.geometry import Point
p = Point(0, 0).buffer(10.0)
len(p.exterior.coords)
p.area

################################################################################
q = Point(0, 0).buffer(10.0, 1)
len(q.exterior.coords)
q.area

################################################################################
from shapely.geometry import Polygon
coords = [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0),
    (1, 1), (0, 0)]

bowtie = Polygon(coords)
bowtie.is_valid

################################################################################
clean = bowtie.buffer(0)
clean.is_valid

################################################################################
len(clean)
list(clean[0].exterior.coords)
list(clean[1].exterior.coords)

################################################################################
Point(0, 0).convex_hull.wkt
from shapely.geometry import MultiPoint
MultiPoint([(0, 0), (1, 1)]).convex_hull.wkt
MultiPoint([(0, 0), (1, 1), (1, -1)]).convex_hull.wkt

################################################################################
Point(0, 0).envelope.wkt

################################################################################
MultiPoint([(0,1), (2, 1), (3, 1)]).envelope.wkt

################################################################################
MultiPoint([(1,0),(3,0.6),(1.5,2),(0,1.4)]).envelope.wkt

################################################################################
p = Point(0.0, 0.0)
x = p.buffer(1.0)

################################################################################
x.area
len(x.exterior.coords)

################################################################################
s = x.simplify(0.05, preserve_topology=False)
s.area
len(s.exterior.coords)
