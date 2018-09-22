#!/usr/bin/env python

import os
import mapnik
from helper.textool import get_tmp_file

stylesheet = os.path.splitext(os.path.realpath(__file__))[0] + '.xml'

m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()

lyrs = m.layers
bbox = None
for lyr in lyrs:
    bbox = lyr.envelope()

b2box = mapnik.Box2d(bbox[0], bbox[1] - 10, bbox[2] + 50, bbox[3] + 50)
m.zoom_to_box(b2box)
mapnik.render_to_file(m, get_tmp_file(__file__, 1))
mapnik.render_to_file(m, get_tmp_file(__file__, 1, file_ext='pdf'))
