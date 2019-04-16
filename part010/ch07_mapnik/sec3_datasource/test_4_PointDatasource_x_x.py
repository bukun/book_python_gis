#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
import mapnik
stylesheet = '/gdata/world_population.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)
s.rules.append(r)
m.append_style('My Style2', s)
###############################################################################
wkt_geom = 'POLYGON ((5 21,-18 -10, -16 -52, 37 -21, 5 21))'
csv_string = '''
     wkt,Name
    "{wkt_geom}","test"
    '''.format(wkt_geom = wkt_geom)
ds = mapnik.Datasource(
    **{"type": "csv", "inline": csv_string})
layer2 = mapnik.Layer('world', '+proj=latlong +datum=WGS84')
layer2.datasource = ds
layer2.styles.append('My Style2')
m.layers.append(layer2)
m.zoom_all()
mapnik.render_to_file(m, 'xx_ds_pt.png', 'png')
