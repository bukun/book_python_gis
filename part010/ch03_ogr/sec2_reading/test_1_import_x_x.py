# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import ogr

################################################################################
from osgeo import ogr

################################################################################
try:
    from osgeo import ogr

except:
    import ogr
