# -*- coding: utf-8 -*-

import os
import mapnik
from helper.textool import get_tmp_file

stylesheet = os.path.splitext(os.path.realpath(__file__))[0] + '.xml'

# image = 'xx_world_style_from_xml.png'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()
# m.background = mapnik.Color('steelblue')


m.zoom_all()

mapnik.render_to_file(m, get_tmp_file(__file__, 1))
mapnik.render_to_file(m, get_tmp_file(__file__, 1, file_ext='pdf'))