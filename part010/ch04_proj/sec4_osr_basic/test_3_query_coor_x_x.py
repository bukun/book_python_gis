# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
from osgeo import osr
sr = osr.SpatialReference()
sr.SetProjCS( 'UTM 17 (WGS84) in northern hemisphere.' )
sr.SetWellKnownGeogCS( 'WGS84' )
sr.SetUTM( 17, True )
sr.IsGeographic()
sr.IsProjected()
################################################################################
srs = osr.SpatialReference()
from osgeo import gdal
srs.ImportFromUSGS(8, 0,
  (0.0, 0.0,
  gdal.DecToPackedDMS(47.0), gdal.DecToPackedDMS(62.0),
  gdal.DecToPackedDMS(45.0), gdal.DecToPackedDMS(54.5),
  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
  15)
srs.GetProjParm(osr.SRS_PP_STANDARD_PARALLEL_1)
srs.GetProjParm(osr.SRS_PP_STANDARD_PARALLEL_2)
srs.GetProjParm(osr.SRS_PP_LATITUDE_OF_CENTER)
srs.GetProjParm(osr.SRS_PP_LONGITUDE_OF_CENTER)
srs.GetProjParm(osr.SRS_PP_FALSE_EASTING)
srs.GetProjParm(osr.SRS_PP_FALSE_NORTHING)
