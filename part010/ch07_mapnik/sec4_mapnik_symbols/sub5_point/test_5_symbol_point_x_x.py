#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os, mapnik
from gispy_helper import renderit
shpfile='/gdata/fig_data/fig_data_poly.shp'
ply_sym = mapnik.PolygonSymbolizer()
ply_sym.fill = mapnik.Color('#f2eff9')
li_sym = mapnik.LineSymbolizer()
pt_sym = mapnik.PointSymbolizer()
m = renderit(point_sym=pt_sym, line_sym=li_sym,
    poly_sym=ply_sym,shpfile=shpfile)
m.zoom_all()
mapnik.render_to_file(m, 'xx_point_sym1.png')
###############################################################################
pt_sym.file = '/gdata/fig_data/turtle.png'
pt_sym.opacity = .8
m = renderit(point_sym=pt_sym, line_sym=li_sym,
    poly_sym=ply_sym,shpfile=shpfile)
m.zoom_all()
mapnik.render_to_file(m, 'xx_point_sym2.png')
###############################################################################
