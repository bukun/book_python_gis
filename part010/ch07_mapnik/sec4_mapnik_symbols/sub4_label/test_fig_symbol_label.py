# -*- coding: utf-8 -*-
import os

import mapnik
from helper.textool import get_tmp_file


def renderit(poly_sym=None, fig_index=0):
    # mapnik.Color('y')
    m = mapnik.Map(600, 200, "+proj=latlong +datum=WGS84")
    # m.background = mapnik.Color('steelblue')
    s = mapnik.Style()
    r = mapnik.Rule()
    # polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))


    # polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('blue'))
    r.symbols.append(poly_sym)
    # line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)


    line_symbolizer = mapnik.LineSymbolizer()
    line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
    line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
    line_symbolizer.stroke_width = 5.0

    # line_symbolizer.stroke_width = 0.1
    # line_symbolizer.stroke_dasharray( [5,10])

    r.symbols.append(line_symbolizer)
    s.rules.append(r)
    m.append_style('My Style', s)
    lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
    lyr.datasource = mapnik.Shapefile(
        file=os.path.join(os.path.dirname(__file__), '/gdata/fig_data/fig_data_line3.shp')
    )
    lyr.styles.append('My Style')
    m.layers.append(lyr)


    m.zoom_all()
    # mapnik.render_to_file(m, 'xx_world_fk.png', 'png')
    mapnik.render_to_file(m, get_tmp_file(__file__, fig_index))
    mapnik.render_to_file(m, get_tmp_file(__file__, fig_index, file_ext='pdf'))


# polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer = mapnik.TextSymbolizer()

polygon_symbolizer.stroke = mapnik.Color('#2eff90')
polygon_symbolizer.stroke.name = mapnik.Expression('[name]')
polygon_symbolizer.stroke.name = 'name'

polygon_symbolizer.stroke.face_name="DejaVu Sans Book"

print('=' * 40)

print(dir(polygon_symbolizer))


print('=' * 40)
print(dir(polygon_symbolizer.stroke))
# polygon_symbolizer.

#mapnik.Expression('[FIELD_NAME]'), "DejaVu Sans Book", 10, mapnik.Color("black")
#polygon_symbolizer.fill = mapnik.Color('#f2eff9')

fig_index = 0
fig_index += 1
# renderit(polygon_symbolizer, fig_index)

# polygon_symbolizer.fill = mapnik.Color('#ff0000')
# fig_index += 1
# renderit(polygon_symbolizer, fig_index)
