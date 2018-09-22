# -*- coding: utf-8 -*-

from helper.textool import get_tmp_file
import os
from mpl_toolkits.basemap import Basemap

# import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10, 6)

map = Basemap(projection='merc',
              lat_0=0, lon_0=0,
              llcrnrlon=-20., llcrnrlat=0., urcrnrlon=180., urcrnrlat=80.)

# map.drawmapboundary(fill_color='aqua')
map.drawmapboundary(fill_color='white')
# map.fillcontinents(color='coral', lake_color='aqua')
map.fillcontinents(color='#eeeeee', lake_color='#eeeeee')
map.drawcoastlines(color="#999999")

map.drawparallels(range(0, 90, 20))
map.drawmeridians(range(0, 180, 20))

# Paris-Tokyo
map.drawgreatcircle(2.3, 48.9, 139.7, 35.6, linewidth=2, color='k')
# Tokyo-Dubai
map.drawgreatcircle(139.7, 35.6, 55.2, 25., linewidth=2, color='k')
# Dubai-Paris
map.drawgreatcircle(55.2, 25., 2.3, 48.9, linewidth=2, color='k')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1', file_ext='png'))
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'))

plt.clf()