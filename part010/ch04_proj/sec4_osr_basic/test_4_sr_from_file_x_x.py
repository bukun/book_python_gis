#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
from osgeo import osr
dataset = gdal.Open("/gdata/geotiff_file.tif")
###############################################################################
sr = dataset.GetProjectionRef()
osrobj = osr.SpatialReference()
osrobj.ImportFromWkt(sr)
###############################################################################
osrobj.ExportToWkt()
osrobj.MorphToESRI()
###############################################################################
osrobj.ExportToWkt()
###############################################################################
osrobj.IsGeographic()
osrobj.IsProjected()
###############################################################################
dataset2 = gdal.Open("/gdata/lu75c.tif")
sr2 = dataset2.GetProjectionRef()
osrobj2 = osr.SpatialReference()
osrobj2.ImportFromWkt(sr2)
osrobj2.IsSame(osrobj)
###############################################################################
osrobj3 = osr.SpatialReference()
osrobj3.SetWellKnownGeogCS("WGS84")
osrobj3.IsSame(osrobj2)
osrobj3.IsSame(osrobj)
osrobj3.ExportToWkt()
osrobj3.IsGeographic()
###############################################################################
from osgeo import ogr, osr
driver = ogr.GetDriverByName('ESRI Shapefile')
dataset = driver.Open('/gdata/GSHHS_c.shp')
layer = dataset.GetLayer()
spatialRef = layer.GetSpatialRef()
spatialRef.ExportToWkt()
spatialRef.ExportToPCI()
spatialRef.ExportToUSGS()
spatialRef.ExportToXML()
###############################################################################
from osgeo import ogr, osr
spatialRef = osr.SpatialReference()
spatialRef.ImportFromEPSG(26912)
spatialRef.MorphToESRI()
with open('xx_proj.prj', 'w') as fout:
    fout.write(spatialRef.ExportToWkt())
