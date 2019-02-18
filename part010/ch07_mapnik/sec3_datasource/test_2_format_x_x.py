# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import mapnik
ds = mapnik.Shapefile(file="/gdata/GSHHS_c.shp")

################################################################################
ds = mapnik.Shapefile(file="/gdata/GSHHS_c.shp",
    encoding="latin1")

################################################################################

ds = mapnik.SQLite(file="spalite.db", table="pcapital",
    geometry_field="geom", key_field="name")
