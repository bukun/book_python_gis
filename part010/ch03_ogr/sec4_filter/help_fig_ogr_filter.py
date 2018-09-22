################################################################
from helper.textool import get_tmp_file
import os
import mapnik
from osgeo import ogr

def create_shp_by_layer(shp, layer):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    outputfile = shp
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver.CreateDataSource(outputfile)
    pt_layer = newds.CopyLayer(layer, '')
    newds.Destroy()

def renderit(shpfile = '', sig=''):
    poly_sym = mapnik.PolygonSymbolizer()
    poly_sym.fill = mapnik.Color('#f2eff9')
    # mapnik.Color('y')
    m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")
    # m.background = mapnik.Color('steelblue')
    s = mapnik.Style()
    r = mapnik.Rule()
    # polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))


    # polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('blue'))
    r.symbols.append(poly_sym)
    # line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)


    line_symbolizer = mapnik.LineSymbolizer()
    line_symbolizer.stroke = mapnik.Color('#000000')
    line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
    line_symbolizer.stroke_width = 1.2

    # line_symbolizer.stroke_width = 0.1
    # line_symbolizer.stroke_dasharray( [5,10])

    r.symbols.append(line_symbolizer)
    s.rules.append(r)
    m.append_style('My Style', s)
    lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
    lyr.datasource = mapnik.Shapefile(file=shpfile)
    lyr.styles.append('My Style')
    m.layers.append(lyr)

    # bbox = mapnik.Box2d(70, 20, 135, 57)

    m.zoom_all()
    # mapnik.render_to_file(m, 'xx_world_fk.png', 'png')
    mapnik.render_to_file(m, get_tmp_file(__file__, sig))
    mapnik.render_to_file(m, get_tmp_file(__file__, sig, file_ext='pdf'), 'pdf')