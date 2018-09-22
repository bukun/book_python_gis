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
box = mapnik.Box2d(env.minx - .2, env.miny - .2, env.maxx + .1, env.maxy + .2)
m.zoom_to_box(box)


mapnik.render_to_file(m, get_tmp_file(__file__, 1))
mapnik.render_to_file(m, get_tmp_file(__file__, 1, file_ext='pdf'))

for x in m.styles:
    for y in x[1].rules:
        for z in y.symbols:
            tt = z.extract()
            print('=' * 20)
            print(dir(z.extract()))
            try:
                print('x' * 60)
                print(tt.name())
                print('x' * 60)
            except:
                pass
            print('-' * 10)

            print(dir(z.symbol))
            print(z.type)
