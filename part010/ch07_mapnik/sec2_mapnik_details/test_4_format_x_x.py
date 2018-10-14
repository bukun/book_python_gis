# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################
import mapnik
mapfile = '/gdata/world_population.xml'
m = mapnik.Map(1000, 500, '+proj=latlong +datum=WGS84')
mapnik.load_map(m, mapfile)

################################################################################
m.zoom_all()

# mapnik.render_to_file(m, 'map.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '1'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '1',file_ext='pdf'), 'pdf')

################################################################################

# mapnik.render_to_file(map, 'map.png', 'png256')

mapnik.render_to_file(m, get_tmp_file(__file__, '2'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '2',file_ext='pdf'), 'pdf')

################################################################################

################################################################################

################################################################################

################################################################################
