# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
import gdal
driver = gdal.GetDriverByName( 'GTiff' )
dst_filename = '/tmp/x_tmp.tif'
dst_ds = driver.Create( dst_filename, 512, 512, 1, gdal.GDT_Byte )
################################################################################
import numpy, osr
dst_ds.SetGeoTransform( [ 444720, 30, 0, 3751320, 0, -30 ] )
srs = osr.SpatialReference()
srs.SetUTM( 11, 1 )
srs.SetWellKnownGeogCS( 'NAD27' )
dst_ds.SetProjection( srs.ExportToWkt() )
raster = numpy.zeros( (512, 512) )
dst_ds.GetRasterBand(1).WriteArray( raster )
################################################################################
