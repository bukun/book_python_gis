# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import osr
osrs = osr.SpatialReference()
osrs.SetGeogCS( "My geographic coordinate system",
  "WGS_1984",
  "My WGS84 Spheroid",
  osr.SRS_WGS84_SEMIMAJOR, osr.SRS_WGS84_INVFLATTENING,
  "Greenwich", 0.0,
  osr.SRS_UA_DEGREE_CONV )

################################################################################

osrs.SetWellKnownGeogCS("WGS84")

################################################################################
osrs.SetWellKnownGeogCS("EPSG:4326")

################################################################################
wkt = osrs.ExportToWkt()
wkt

################################################################################
wkt2 = osrs.ExportToPrettyWkt()
print(wkt2)

################################################################################
sr = osr.SpatialReference()
sr.SetProjCS( 'UTM 17 (WGS84) in northern hemisphere.' )
wkt = sr.ExportToWkt()
wkt

################################################################################
sr.SetWellKnownGeogCS( 'WGS84' )
wkt = sr.ExportToWkt()
wkt

################################################################################
sr2 = osr.SpatialReference()
sr2.SetUTM( 17, True )
sr2.SetWellKnownGeogCS( 'WGS84' )

################################################################################
wkt2 = sr2.ExportToPrettyWkt()
print(wkt2)
