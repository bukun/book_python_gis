# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
from pyproj import Proj
albers=Proj('+proj=aea +lon_0=105 +lat_1=25 +lat_2=47 +ellps=krass')
albers_x,albers_y=albers(105,36)
albers_x,albers_y
################################################################################
utm=Proj(proj='utm',zone=48,ellps='krass')
utm_x,utm_y=utm(105,36)
print(utm_x,utm_y )
################################################################################
from pyproj import transform
to_utm_x,to_utm_y = transform(albers,utm,albers_x ,albers_y)
print(to_utm_x,to_utm_y )
