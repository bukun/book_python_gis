#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
lines = [((0, 0), (2, 2)),
         ((0, 0), (0, 2)),
         ((0, 2), (2, 2)),
         ((2, 2), (2, 0)),
         ((2, 0), (0, 0))]
###############################################################################
from shapely.ops import linemerge
the_lines = linemerge(lines)
for aline in the_lines:
    print(aline)

###############################################################################
from shapely.ops import polygonize
the_polys = polygonize(lines)
for apoly in the_polys:
    print(apoly)

