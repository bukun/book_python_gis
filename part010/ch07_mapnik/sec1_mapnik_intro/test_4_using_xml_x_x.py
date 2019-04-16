#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
stylesheet = '/gdata/world_style.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()
mapnik.render_to_file(m,'xworld2.png', 'png')
###############################################################################
