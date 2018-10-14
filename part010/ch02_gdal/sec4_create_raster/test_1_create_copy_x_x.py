# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################
import gdal
src_filename = "/gdata/geotiff_file.tif"
dst_filename = "/tmp/xx_geotiff_copy.tif"
driver = gdal.GetDriverByName('GTiff')
src_ds = gdal.Open( src_filename )
dst_ds = driver.CreateCopy( dst_filename, src_ds, 0 )

################################################################################
dst_filename2 = "/tmp/xx_geotiff_copy2.tif"
dst_ds = driver.CreateCopy( dst_filename2, src_ds, 0,
   [ 'TILED=YES', 'COMPRESS=PACKBITS' ] )

dst_filename3 = "/tmp/xx_geotiff_copy3.tif"
dst_ds3 = driver.CreateCopy( dst_filename3, src_ds, 0,
   [ 'TILED=YES', 'COMPRESS=PACKBITS' ] )

################################################################################

driver.CreateCopy("/tmp/xx_geotiff_copy_a1.tif",src_ds,0)

################################################################################
driver.CreateCopy("/tmp/xx_geotiff_copy_a2.tif",src_ds,0,["INTERLEAVE=PIXEL"])
