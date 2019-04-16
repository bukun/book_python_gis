#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
###############################################################################
bsmap = Basemap()
###############################################################################
bsmap.drawcoastlines()
plt.show()
###############################################################################
plt.savefig('xx_test.png')
###############################################################################
bsmap = Basemap(projection='ortho',lat_0=0, lon_0=105)
bsmap.drawmapboundary(fill_color='aqua')
###############################################################################
bsmap.fillcontinents(color= 'coral',lake_color='aqua')
bsmap.drawcoastlines()
plt.show()
###############################################################################
plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window
