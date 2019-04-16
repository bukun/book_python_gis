#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
nmap = mapnik.Map(600, 400)
###############################################################################
nmap.srs
###############################################################################
style1, style2, style3 = [mapnik.Style()] * 3
nmap.append_style("s1", style1)
nmap.append_style("s2", style2)
nmap.append_style("s3", style1)
nmap.append_style("s1", style3)
###############################################################################
layer = mapnik.Layer('lyrname')
layer.srs
###############################################################################
ds = mapnik.Shapefile(file='/gdata/GSHHS_c.shp')
layer.datasource = ds
layer.styles.append("s1")
layer.styles.append("s2")
###############################################################################
nmap.layers.append(layer)
