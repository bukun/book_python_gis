#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
from gispy_helper import renderit
shpfile = '/gdata/fig_data/fig_data_poly.shp'
symbolizer = mapnik.PolygonSymbolizer()
###############################################################################
symbolizer.fill = mapnik.Color("steelblue")
linesym = mapnik.LineSymbolizer()
m = renderit(line_sym=linesym, poly_sym=symbolizer,
    shpfile = shpfile)
mapnik.render_to_file(m, 'xx_mnik_poly_out.png')
###############################################################################
symbolizer.fill_opacity = 0.5
m = renderit(line_sym=linesym, poly_sym=symbolizer,
    shpfile = shpfile)
mapnik.render_to_file(m, 'xx_mnik_poly_out2.png')
###############################################################################
linesym.stroke = mapnik.Color('rgb(50%,50%,50%)')
linesym.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
linesym.stroke_width = 5.0
###############################################################################
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
###############################################################################
m = renderit(line_sym=linesym, poly_sym=polygon_symbolizer,
   shpfile = shpfile)
mapnik.render_to_file(m, 'xx_mnik_poly_out3.png')
###############################################################################
