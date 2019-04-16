#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
datasource = mapnik.Gdal(file="/gdata/foo.tif")
###############################################################################
datasource = mapnik.Ogr(file="/gdata/region_popu.shp",
    layer="region_popu")
