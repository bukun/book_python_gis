# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import mapnik
ds = mapnik.Shapefile(file='/gdata/GSHHS_c.shp')
ds.envelope()

################################################################################
import os
stylesheet = '/gdata/world_map.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
for x in m.layers:
    print(x.name)
    print(x.envelope())
