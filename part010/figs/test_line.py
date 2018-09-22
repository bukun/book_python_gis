# -*- coding: utf-8 -*-

from matplotlib import pyplot
from shapely.geometry import LineString
from descartes import PolygonPatch

from helper.textool import get_tmp_file
from osgeo import ogr

BLUE = '#6699cc'
GRAY = '#999999'


def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)


line = LineString([(100, 100), (101, 101), (100, 102), (102, 102), (103, 101), (101, 100)])

fig = pyplot.figure(1, figsize=(10, 4), dpi=180)

# 1
ax = fig.add_subplot(121)

plot_line(ax, line)

# 2
ax = fig.add_subplot(122)

# GeoJSON-like data works as well

# >>> geo['type']
# 'Polygon'
# >>> geo['coordinates'][0][:2]
# ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))



ds = ogr.Open('/gdata/GSHHS_c.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
while feat:

    fd_val = feat.GetField("AREA")
    if fd_val != 9596900 :
        print('Got it')
        geom = feat.GetGeometryRef()
        pts = geom.GetGeometryCount()
        for ii in range(pts):

            poly = geom.GetGeometryRef(ii)
            points_num = poly.GetPointCount()
            print(points_num)
            zc_points = poly.GetPoints()
            # print(type(zc_points))
            tmp_pt_arr = []
            for x in zc_points:
                tmp_pt_arr.append(x)

            pt = LineString(tmp_pt_arr)
        print('Got the line')
        # break
    else:
        pass
    feat = layer.GetNextFeature()

print('begin drawing ...')
fig2 = pyplot.figure(1, figsize=(10, 4), dpi=180)

plot_line(ax, pt)

print('finished drawing ...')
# GeoJSON-like data works as well

# >>> geo['type']
# 'Polygon'
# >>> geo['coordinates'][0][:2]
# ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))

# pyplot.savefig('figs/xx_data_line.png')

pyplot.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight')
pyplot.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight')
pyplot.clf()