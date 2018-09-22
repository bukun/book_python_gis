# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
lines = [((0, 0), (2, 2)),
         ((0, 0), (0, 2)),
         ((0, 2), (2, 2)),
         ((2, 2), (2, 0)),
         ((2, 0), (0, 0))]
################################################################################
from shapely.ops import linemerge
the_lines = linemerge(lines)
for aline in the_lines:
    print(aline)

################################################################################
from shapely.ops import polygonize
the_polys = polygonize(lines)
for apoly in the_polys:
    print(apoly)

