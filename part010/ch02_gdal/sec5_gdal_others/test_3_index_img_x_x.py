# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################


################################################################################
from osgeo import gdal
dataset = gdal.Open('/gdata/lu75c.tif')
band = dataset.GetRasterBand(1)
band.GetRasterColorInterpretation()
1
################################################################################
from osgeo import gdalconst
dir(gdalconst)
gdalconst.GPI_CMYK
gdalconst.GPI_Gray
gdalconst.GPI_HLS
gdalconst.GPI_RGB
gdalconst.GDT_Byte
################################################################################
colormap = band.GetRasterColorTable()
colormap is None
################################################################################
dataset = gdal.Open('/gdata/lu75i1.tif')
band = dataset.GetRasterBand(1)
band.GetRasterColorInterpretation()
################################################################################
from osgeo import gdalconst
gdalconst.GCI_PaletteIndex
################################################################################
colormap = band.GetRasterColorTable()
dir(colormap)
colormap.GetCount()
################################################################################
colormap.GetPaletteInterpretation()
gdalconst.GPI_RGB
################################################################################
for i in range(colormap.GetCount()):
    print("%i:%s" % (i, colormap.GetColorEntry(i)))

################################################################################
################################################################################
