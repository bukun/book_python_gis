# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import gdal
format = "GTiff"
driver = gdal.GetDriverByName( format )
metadata = driver.GetMetadata()
if gdal.DCAP_CREATE in metadata and metadata[gdal.DCAP_CREATE] == 'YES':
    print ('Driver %s supports Create() method.' % format)


if gdal.DCAP_CREATECOPY in metadata and metadata[gdal.DCAP_CREATECOPY] == 'YES':
    print ('Driver %s supports CreateCopy() method.' % format)

