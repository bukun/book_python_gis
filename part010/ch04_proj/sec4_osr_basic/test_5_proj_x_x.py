# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from osgeo import osr
source = osr.SpatialReference()
source.ImportFromEPSG(2927)
target = osr.SpatialReference()
target.ImportFromEPSG(4326)
transform = osr.CoordinateTransformation(source, target)
transform.TransformPoint(609000,4928000)

################################################################################
from osgeo import ogr
point = ogr.CreateGeometryFromWkt(
    "POINT (1120351.57 741921.42)")

point.Transform(transform)
point.ExportToWkt()

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################
