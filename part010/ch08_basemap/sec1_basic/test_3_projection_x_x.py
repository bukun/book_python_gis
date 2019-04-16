#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mpl_toolkits.basemap
print(mpl_toolkits.basemap.supported_projections)
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
bsmap = Basemap(projection='cyl')
bsmap.drawcoastlines()
bsmap.drawmeridians(np.arange(0, 360, 30))
bsmap.drawparallels(np.arange(-90, 90, 30))
plt.show()
###############################################################################
bsmap = Basemap(projection='aeqd', lon_0=180, lat_0=50)
bsmap.drawmapboundary()
bsmap.drawcoastlines()
plt.show()
###############################################################################
bsmap = Basemap(projection='mbtfpq', lon_0=105)
bsmap.drawcoastlines()
bsmap.drawmeridians(np.arange(0, 360, 30))
bsmap.drawparallels(np.arange(-90, 90, 30))
plt.show()
###############################################################################
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
bsmap = Basemap(projection='aeqd', lon_0 = 10, lat_0 = 50)
bsmap(10,50)
###############################################################################
bsmap(20015077.3712, 20015077.3712, inverse=True)
