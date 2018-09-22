#!/usr/bin/env python

import os
import mapnik
from helper.textool import get_tmp_file

stylesheet = os.path.splitext(os.path.realpath(__file__))[0] + '.xml'

# image = 'xx_world_style_from_xml.png'
m = mapnik.Map(600, 150)
mapnik.load_map(m, stylesheet)
m.zoom_all()
# m.background = mapnik.Color('steelblue')

# bbox = mapnik.Box2d(118, 36.6, 124.6, 40.7)
bbox = mapnik.Box2d(-1, -1, 8, 1)
m.zoom_to_box(bbox)
mapnik.render_to_file(m, get_tmp_file(__file__, 1))
mapnik.render_to_file(m, get_tmp_file(__file__, 1, file_ext='pdf'))




# stylesheet = os.path.splitext(os.path.realpath(__file__))[0] + '1.xml'
#
# # image = 'xx_world_style_from_xml.png'
# m = mapnik.Map(600, 300)
# mapnik.load_map(m, stylesheet)
# m.zoom_all()
# # m.background = mapnik.Color('steelblue')
#
# # bbox = mapnik.Box2d(118, 36.6, 124.6, 40.7)
#
# m.zoom_to_box(bbox)
# mapnik.render_to_file(m, get_tmp_file(__file__, 2), 'png')
