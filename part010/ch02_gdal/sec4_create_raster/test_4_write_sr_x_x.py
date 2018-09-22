# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
import osr
import gdal
dataset = gdal.Open("/gdata/geotiff_file.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
datas = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
tods = driver.Create("/tmp/x_geotiff_file_3.tif",width,height,3,options=["INTERLEAVE=PIXEL"])
tods.SetGeoTransform( [ 444720, 30, 0, 3751320, 0, -30 ] )
srs = osr.SpatialReference()
srs.SetUTM( 11, 1 )
srs.SetWellKnownGeogCS( 'NAD27' )
tods.SetProjection( srs.ExportToWkt() )
