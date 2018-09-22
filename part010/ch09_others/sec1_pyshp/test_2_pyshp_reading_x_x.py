# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import shapefile
sf = shapefile.Reader("/gdata/GSHHS_c")
sf2 = shapefile.Reader("/gdata/GSHHS_c.shp")
sf3 = shapefile.Reader("/gdata/GSHHS_c.dbf")
################################################################################
myshp = open("/gdata/GSHHS_c.shp", "rb")
mydbf = open("/gdata/GSHHS_c.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)
################################################################################
shapes = sf.shapes()
len(shapes)
################################################################################
len(list(sf.iterShapes()))
################################################################################
for name in dir(shapes[3]):
    if not name.startswith('__'):
        name
################################################################################
shapes[3].shapeType
################################################################################
bbox = shapes[3].bbox
['%.3f' % coord for coord in bbox]
################################################################################
shapes[3].parts
################################################################################
len(shapes[3].points)
################################################################################
shape = shapes[3].points[7]
['%.3f' % coord for coord in shape]
################################################################################
s = sf.shape(7)
['%.3f' % coord for coord in s.bbox]
################################################################################
fields = sf.fields
fields
################################################################################
records = sf.records()
len(records)
################################################################################
len(list(sf.iterRecords()))
################################################################################
rec = sf.record(3)
rec[1:3]
################################################################################
records[3][1:3]
################################################################################
shapeRecs = sf.shapeRecords()
################################################################################
shapeRecs[0].shape.shapeType
################################################################################
shapeRecs[0].record[1:3]
################################################################################
points = shapeRecs[3].shape.points[0:2]
len(points)
################################################################################
shapeRec = sf.shapeRecord(3)
shapeRec.record[1:3]
points = shapeRec.shape.points[0:2]
len(points)
################################################################################
shapeRecs = sf.iterShapeRecords()
for shapeRec in shapeRecs:
    # do something here
    pass
################################################################################
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.axes().set_aspect('equal', 'box')
################################################################################
sf = shapefile.Reader('/gdata/GSHHS_l_L1.shp')
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x, y, linewidth = .6, color='darkslategray')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
s = sf.shape(0)
s.__geo_interface__["type"]
