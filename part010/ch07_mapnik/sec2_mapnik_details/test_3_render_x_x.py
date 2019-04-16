#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
import cairo
import os
mapfile = '/gdata/world_population.xml'
projection = '+proj=latlong +datum=WGS84'
m = mapnik.Map(1000, 500)
mapnik.load_map(m, mapfile)
bbox = mapnik.Box2d(-180.0,-90.0,180.0,90.0)
m.zoom_to_box(bbox)
mapnik.render_to_file(m, 'xx_a.png', 'png')
###############################################################################
surface = cairo.SVGSurface('xx_a.svg', m.width, m.height)
mapnik.render(m, surface)
surface.finish()
###############################################################################
surface = cairo.PDFSurface('xx_a.pdf', m.width, m.height)
mapnik.render(m, surface)
surface.finish()
