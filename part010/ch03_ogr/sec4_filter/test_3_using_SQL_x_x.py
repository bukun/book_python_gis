# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from osgeo import ogr
import os
def create_shp_by_layer(shp, layer):
    outputfile = shp
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver. CreateDataSource ( outputfile )
    pt_layer = newds.CopyLayer ( layer, '')
    newds.Destroy ()
################################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = '/gdata/GSHHS_h.shp'
world_ds = ogr.Open(world_shp)
world_layer = world_ds.GetLayer()
world_layer.GetFeatureCount()
################################################################################
world_layer_name = world_layer.GetName()
result = world_ds.ExecuteSQL("SELECT * FROM {lyr} WHERE AREA > 800000".format(lyr=world_layer_name))
result.GetFeatureCount()
################################################################################
resultFeat = result.GetNextFeature ()
out_shp = '/tmp/sql_res.shp'
create_shp_by_layer(out_shp, result)
world_ds.ReleaseResultSet(result)
