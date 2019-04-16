#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
ds = mapnik.Shapefile(file="/gdata/GSHHS_c.shp")
###############################################################################
ds = mapnik.Shapefile(file="/gdata/GSHHS_c.shp",
    encoding="latin1")
###############################################################################
ds = mapnik.SQLite(file="spalite.db", table="pcapital",
    geometry_field="geom", key_field="name")
