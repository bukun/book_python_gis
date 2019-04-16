#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################


###############################################################################
from osgeo import gdal
dataset = gdal.Open('/gdata/lu75c.tif')
band = dataset.GetRasterBand(1)
band.GetRasterColorInterpretation()
1
###############################################################################
from osgeo import gdalconst
dir(gdalconst)
gdalconst.GPI_RGB
gdalconst.GDT_Byte
###############################################################################
colormap = band.GetRasterColorTable()
colormap is None
###############################################################################
dataset = gdal.Open('/gdata/lu75i1.tif')
band = dataset.GetRasterBand(1)
band.GetRasterColorInterpretation()
gdalconst.GCI_PaletteIndex
###############################################################################
colormap = band.GetRasterColorTable()
dir(colormap)
colormap.GetCount()
###############################################################################
gdalconst.GPI_Gray, gdalconst.GPI_RGB, gdalconst.GPI_CMYK, \
    gdalconst.GPI_HLS
###############################################################################
colormap.GetPaletteInterpretation()
gdalconst.GPI_RGB
###############################################################################
for i in range(colormap.GetCount()):
    print("{}:{}".format(i, colormap.GetColorEntry(i)))

