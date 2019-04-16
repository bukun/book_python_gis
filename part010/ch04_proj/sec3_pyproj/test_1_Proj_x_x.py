#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from pyproj import Proj
p=Proj(
  '+proj=aea +lon_0=105 +lat_1=25 +lat_2=47 +ellps=krass')
x,y=p(105,36)
print('%.3f,%.3f' %(x,y))
###############################################################################
Proj(proj='utm',zone=10,ellps='WGS84') # use kwargs
Proj('+proj=utm +zone=10 +ellps=WGS84') # use Proj.4 string
Proj(init="epsg:32667")
Proj("+init=epsg:32667",preserve_units=True)
###############################################################################
lon,lat=p(x,y,inverse=True)
print('%.3f,%.3f' %(lon,lat))
###############################################################################
import math
x,y=p(math.radians(105),math.radians(36),radians=True)
print( '%.3f,%.3f' %(x,y) )
###############################################################################
lons=(105,106,104)
lats=(36,35,34)
x,y=p(lons,lats)
###############################################################################
print('%.3f,%.3f,%.3f' %x)
print('%.3f,%.3f,%.3f' %y)
type(x)
###############################################################################
utm=Proj(proj='utm',zone=48,ellps='WGS84')
###############################################################################
x,y=utm(105,36)
x,y
###############################################################################
utm.is_geocent()
utm.is_latlong()
latlong=Proj('+proj=latlong')
latlong.is_latlong()
latlong.is_geocent()
