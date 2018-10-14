# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import ogr
import os,math
inshp = '/gdata/GSHHS_c.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = '/tmp/xx_GSHHS_copy1.shp'
if os.access( outputfile, os.F_OK ):
    driver.DeleteDataSource(outputfile)

pt_cp = driver.CopyDataSource(ds, outputfile)
pt_cp.Release()

################################################################################
outputfile = '/tmp/xx_GSHHS_copy2.shp'
if os.access(outputfile, os.F_OK):
    driver.DeleteDataSource(outputfile)

layer = ds.GetLayer()
newds = driver.CreateDataSource(outputfile)

################################################################################
pt_layer = newds.CopyLayer(layer, 'abcd')
newds.Destroy()

################################################################################
dir(pt_layer)

################################################################################
outputfile ='/tmp/xx_GSHHS_copy3.shp'
if os.access( outputfile, os.F_OK ):
    driver.DeleteDataSource( outputfile )

newds = driver.CreateDataSource(outputfile)
layernew = newds.CreateLayer('worldcopy',None,ogr.wkbLineString)

################################################################################
layer = ds.GetLayer()
feature = layer.GetNextFeature()
while feature is not None:
    layernew.CreateFeature(feature)
    feature = layer.GetNextFeature()

newds.Destroy()
