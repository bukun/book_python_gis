# -*- coding: utf-8 -*-

from helper.textool import get_tmp_file
import os
from mpl_toolkits.basemap import Basemap

# import numpy as np
import matplotlib

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['STKaiti']
import matplotlib.pyplot as plt

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10, 6)

# lon = 116.41667
lon1 = 91
# lat = 39.91667
lat1 = 29.6
lon2 = 125.35
lat2 = 43.88333

para = {
    # 'projection': 'geos',
    'lat_0': 0,
    'lon_0': 120,
    'resolution': 'l',
    'area_thresh': 1000.0,
    'llcrnrlon': lon1 - 2,
    'llcrnrlat': lat1 - 2,
    'urcrnrlon': lon2 + 2,
    'urcrnrlat': lat2 + 2
}

map = Basemap(**para)

# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral', lake_color='aqua')
map.drawcoastlines()

# map.drawparallels(range(0, 90, 20))
# map.drawmeridians(range(0, 180, 20))

# Dubai-Paris

# plt.show()


map.drawgreatcircle(lon1, lat1, lon2, lat2, linewidth=1.5, color='k')

x1, y1 = map(lon1, lat1)
map.plot(x1, y1, 'ko', markersize=6)
plt.text(x1 - 1, y1 -1.2, '拉萨', fontsize=12, fontweight='bold',
         ha='left', va='bottom', color='k')

x2, y2 = map(lon2, lat2)

map.plot(x2, y2, 'ko', markersize=6)
plt.text(x2 + .3, y2 + .5, '长春', fontsize=12, fontweight='bold',
         ha='left', va='center', color='k',
         )

npts = [
[33.193,   96.847],
[36.486,  103.170],
[39.415,  110.018],
[41.906,  117.418],
    ]

for npt in npts:
    xx, yy = map(npt[1], npt[0])
    map.plot(xx, yy, 'kx', markersize=6)


plt.savefig(get_tmp_file(__file__, '1', file_ext='png'), bbox_inches='tight')
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight')

plt.clf()
