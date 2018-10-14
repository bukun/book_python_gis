# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import mapnik
from gispy_helper import renderit
shpfile = '/gdata/fig_data/fig_data_poly.shp'
symbolizer = mapnik.PolygonSymbolizer()

################################################################################
symbolizer.fill = mapnik.Color("steelblue")
linesym = mapnik.LineSymbolizer()
m = renderit(line_sym=linesym, poly_sym=symbolizer, shpfile = shpfile)

# mapnik.render_to_file(m, 'xx_mnik_poly_out.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '1'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '1',file_ext='pdf'), 'pdf')

################################################################################
symbolizer.fill_opacity = 0.5
m = renderit(line_sym=linesym, poly_sym=symbolizer, shpfile = shpfile)

# mapnik.render_to_file(m, 'xx_mnik_poly_out2.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '2'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '2',file_ext='pdf'), 'pdf')

################################################################################

################################################################################
linesym.stroke = mapnik.Color('rgb(50%,50%,50%)')
linesym.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
linesym.stroke_width = 5.0

################################################################################
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')

################################################################################
m = renderit(line_sym=linesym, poly_sym=polygon_symbolizer, shpfile = shpfile)

# mapnik.render_to_file(m, 'xx_mnik_poly_out3.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '3'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '3',file_ext='pdf'), 'pdf')

################################################################################

################################################################################
