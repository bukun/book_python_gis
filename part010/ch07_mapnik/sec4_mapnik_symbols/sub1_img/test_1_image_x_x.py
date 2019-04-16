#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
m = mapnik.Map(600, 500, "+proj=latlong +datum=WGS84")
symbol = mapnik.RasterSymbolizer()
###############################################################################
s = mapnik.Style()
r = mapnik.Rule()
r.symbols.append(symbol)
s.rules.append(r)
m.append_style('My Style', s)
datasource = mapnik.Gdal(file='/gdata/geotiff_file.tif')
layer = mapnik.Layer("myLayer")
layer.datasource = datasource
layer.styles.append('My Style')
m.layers.append(layer)
###############################################################################
layer.envelope()
###############################################################################
m.zoom_to_box(layer.envelope())
mapnik.render_to_file(m, 'xx_mapnik_result.png', 'png')
