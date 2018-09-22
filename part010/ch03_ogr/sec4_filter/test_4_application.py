# -*- coding: utf-8 -*-

print('=' * 40)
print(__file__)

from osgeo import ogr
world_shp = '/gdata/GSHHS_c.shp'
world_ds = ogr.Open(world_shp)
################################################################################
result = world_ds.ExecuteSQL("select * from GSHHS_c")
result.GetFeatureCount()
result = world_ds.ExecuteSQL("select count(*) from GSHHS_c where AREA>50")
result.GetFeatureCount()
################################################################################
result.GetFeature(0).GetField(0)
################################################################################
world_ds.ReleaseResultSet(result)
################################################################################
result = world_ds.ExecuteSQL("select distinct level from GSHHS_c")
resultFeat = result.GetNextFeature()
while resultFeat:
    print (resultFeat.GetField(0))
    resultFeat = result.GetNextFeature()
world_ds.ReleaseResultSet(result)
################################################################################
# coverLayer = ds.ExecuteSQL('/gdata/select distinct cover from sites')
#coverFeat = coverLayer.GetNextFeature()

# while coverFeat:
#     cntLayer = ds.ExecuteSQL("select count( * from sites where cover = ‘ “ + coverFeat.GetField(0) + “ ‘ “)
#     print (coverFeat.GetField(0) + ' ' +print coverFeat.GetField(0) + ' ' + cntLayer.GetFeature(0).GetFieldAsString(0))
# ds.ReleaseResultSet(cntLayer)
# coverFeat = coverLayer.GetNextFeature()
# ds.ReleaseResultSet(coverLayer)
