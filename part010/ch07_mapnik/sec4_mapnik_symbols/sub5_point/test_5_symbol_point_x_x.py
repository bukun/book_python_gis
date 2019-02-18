# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import os, mapnik
from gispy_helper import renderit
shpfile='/gdata/fig_data/fig_data_poly.shp'
ply_sym = mapnik.PolygonSymbolizer()
ply_sym.fill = mapnik.Color('#f2eff9')
li_sym = mapnik.LineSymbolizer()
pt_sym = mapnik.PointSymbolizer()
m = renderit(point_sym=pt_sym, line_sym=li_sym,
    poly_sym=ply_sym,shpfile=shpfile)

m.zoom_all()

# mapnik.render_to_file(m, 'xx_point_sym1.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '1'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '1',file_ext='pdf'), 'pdf')

################################################################################
pt_sym.file = '/gdata/fig_data/turtle.png'
pt_sym.opacity = .8
m = renderit(point_sym=pt_sym, line_sym=li_sym,
    poly_sym=ply_sym,shpfile=shpfile)

m.zoom_all()

# mapnik.render_to_file(m, 'xx_point_sym2.png')

mapnik.render_to_file(m, get_tmp_file(__file__, '2'), 'png')
mapnik.render_to_file(m, get_tmp_file(__file__, '2',file_ext='pdf'), 'pdf')

################################################################################

################################################################################

################################################################################

################################################################################
