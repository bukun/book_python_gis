# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import os, mapnik
from gispy_helper import renderit
li_sym = mapnik.LineSymbolizer()
m = renderit(line_sym = li_sym)

# mapnik.render_to_file(m, 'xx_mnik_out.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '1'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '1',file_ext='pdf'), 'pdf')

################################################################################
li_sym.stroke = mapnik.Color('rgb(50%,50%,50%)')
li_sym.stroke_width = 15.0
m = renderit(line_sym = li_sym)

# mapnik.render_to_file(m, 'xx_mnik_out2.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '2'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '2',file_ext='pdf'), 'pdf')

################################################################################
li_sym.stroke_opacity = 0.8
m = renderit(line_sym = li_sym)

# mapnik.render_to_file(m, 'xx_mnik_out3.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '3'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '3',file_ext='pdf'), 'pdf')

################################################################################

################################################################################
from gispy_helper import mapnik_lyr
m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")
line_data = '/gdata/fig_data/fig_data_line.shp'
li_sym = mapnik.LineSymbolizer()
li_sym.stroke = mapnik.Color('rgb(50%,50%,50%)')
li_sym.stroke_width = 14.0
ly1 = mapnik_lyr(m, data=line_data, line_sym=li_sym)

################################################################################
line_sym2 = mapnik.LineSymbolizer()
line_sym2.stroke = mapnik.Color("#ffd3a9")
line_sym2.stroke_width = 10.0
line_sym2.stroke_opacity = 0.8
ly2 = mapnik_lyr(m, data=line_data, line_sym=line_sym2)

################################################################################
m.layers.append(ly1)
m.layers.append(ly2)
m.zoom_all()

# mapnik.render_to_file(m, 'out.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '4'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '4',file_ext='pdf'), 'pdf')

################################################################################
line_sym2 = mapnik.LinePatternSymbolizer()
line_sym2.file = '/gdata/fig_data/turtle.png'
m = renderit(line_sym = line_sym2)

# mapnik.render_to_file(m, 'out.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '5'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '5',file_ext='pdf'), 'pdf')

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################
