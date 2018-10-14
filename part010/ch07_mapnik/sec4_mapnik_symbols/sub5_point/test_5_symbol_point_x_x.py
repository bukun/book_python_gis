# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import os, mapnik
from gispy_helper import renderit
shpfile='/gdata/fig_data/fig_data_poly.shp'
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
line_symbolizer = mapnik.LineSymbolizer()
symbolizer = mapnik.PointSymbolizer()
m = renderit(point_sym=symbolizer, line_sym=line_symbolizer, poly_sym=polygon_symbolizer,shpfile=shpfile)
m.zoom_all()

# mapnik.render_to_file(m, 'xx_point_sym1.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '1'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '1',file_ext='pdf'), 'pdf')

################################################################################
symbolizer.file = '/gdata/fig_data/turtle.png'
symbolizer.opacity = .8
m = renderit(point_sym=symbolizer, line_sym=line_symbolizer, poly_sym=polygon_symbolizer,shpfile=shpfile)
m.zoom_all()

# mapnik.render_to_file(m, 'xx_point_sym2.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '2'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '2',file_ext='pdf'), 'pdf')

################################################################################

################################################################################

################################################################################

################################################################################
