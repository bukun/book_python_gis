#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.subplot(121)
bsmap = Basemap(projection='ortho',lon_0=0,
    lat_0=0,resolution='c')
bsmap.drawmapboundary()
plt.subplot(122)
bsmap = Basemap(projection='sinu',lon_0=0,resolution='c')
bsmap.drawmapboundary(fill_color='aqua')
plt.show()
###############################################################################
bsmap = Basemap(projection='poly',
    lon_0=0.0, lat_0=0, llcrnrlon=-80.,
    llcrnrlat=-40,urcrnrlon=80.,urcrnrlat=40.)
bsmap.drawmapboundary()
bsmap.drawcoastlines()
###############################################################################
bsmap.drawmeridians(range(0, 360, 20))
###############################################################################
bsmap.drawparallels(range(-90, 100, 10), linewidth=2,
   dashes=[4, 2], labels=[1,0,0,1], color='r' )
plt.show()
