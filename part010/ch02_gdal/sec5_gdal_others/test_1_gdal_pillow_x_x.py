# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/geotiff_file.tif")
data_arr = dataset.ReadAsArray(30,70,5,5)
type(data_arr)
data_arr
data_bin = dataset.ReadRaster(30,70,5,5)
data_bin

################################################################################
data_arr.tostring()

################################################################################
from PIL import Image
im = Image.open("/gdata/geotiff_file.tif")
region = im.crop((30,70,35,75))
region.tobytes()

################################################################################
import numpy as np
data = dataset.ReadAsArray(30,70,5,5)
from numpy import reshape
datas = [reshape(i,(-1,1)) for i in data]
datas = np.concatenate(datas,1)
datas.tostring()

################################################################################
band = dataset.GetRasterBand(1)
band.ReadRaster(30,70,5,5)

################################################################################
r,g,b = region.split()
r.tobytes()

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################
