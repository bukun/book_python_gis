#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
###############################################################################
m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")
m.background = mapnik.Color('steelblue')
mapnik.render_to_file(m, 'xx_background.png', 'png')
###############################################################################
s = mapnik.Style()
r=mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
###############################################################################
ds = mapnik.Shapefile(file='/gdata/GSHHS_c.shp')
###############################################################################
layer = mapnik.Layer('world')
###############################################################################
layer.datasource = ds
layer.styles.append('My Style')
###############################################################################
m.layers.append(layer)
m.zoom_all()
###############################################################################
mapnik.render_to_file(m,'xworld2.png', 'png')
