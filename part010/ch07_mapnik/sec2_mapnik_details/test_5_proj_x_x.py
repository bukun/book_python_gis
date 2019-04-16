#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
import mapnik
m = mapnik.Map(600, 300, '+init=epsg:4326')
###############################################################################
lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='/gdata/GSHHS_c.shp')
