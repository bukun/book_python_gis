# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import mapnik
stylesheet = '/gdata/world_style.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()

# mapnik.render_to_file(m,'xworld2.png', 'png')

mapnik.render_to_file(m, get_tmp_file(__file__, '1'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '1',file_ext='pdf'), 'pdf')
################################################################################
