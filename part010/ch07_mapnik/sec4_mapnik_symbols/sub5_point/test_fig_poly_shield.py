# -*- coding: utf-8 -*-

import mapnik
from helper.textool import get_tmp_file
import os

stylesheet = os.path.splitext(os.path.realpath(__file__))[0] + '.xml'

m = mapnik.Map(600, 200)
mapnik.load_map(m, stylesheet)

m.zoom_all()
# env = m.envelope()
# print(env)
# box = mapnik.Box2d(env.minx - .1, env.miny - .3, env.maxx + .3, env.maxy + .3)
# m.zoom_to_box(box)

mapnik.render_to_file(m, get_tmp_file(__file__, 1))
mapnik.render_to_file(m, get_tmp_file(__file__, 1, file_ext='pdf'))
