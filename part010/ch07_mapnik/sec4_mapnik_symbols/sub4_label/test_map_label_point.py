# -*- coding: utf-8 -*-

import mapnik
from helper.textool import get_tmp_file
import os

stylesheet = os.path.splitext(os.path.realpath(__file__))[0] + '.xml'

m = mapnik.Map(600, 200)
mapnik.load_map(m, stylesheet)

m.zoom_all()
env = m.envelope()
print(env)
box = mapnik.Box2d(env.minx - .2, env.miny - .2, env.maxx + .2, env.maxy + .2)
m.zoom_to_box(box)



mapnik.render_to_file(m, get_tmp_file(__file__, 2))
mapnik.render_to_file(m, get_tmp_file(__file__, 2, file_ext='pdf'))
