# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import mapnik
datasource = mapnik.Shapefile(file="/gdata/GSHHS_c.shp")

################################################################################
datasource = mapnik.Shapefile(file="/gdata/GSHHS_c.shp", encoding="latin1")

################################################################################
datasource = mapnik.SQLite(file="spalite.db", table="pcapital", geometry_field="geom", key_field="name")
