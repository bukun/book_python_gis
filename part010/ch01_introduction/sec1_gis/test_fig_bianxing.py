from helper.textool import get_tmp_file
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Agg')

fig, ax = plt.subplots(nrows=2, ncols=2)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12.5, 10)
p1 = plt.subplot(221)

# lon_0, lat_0 are the center point of the projection.
# resolution = 'l' means use low resolution coastlines.
m = Basemap(projection='ortho', lon_0=20, lat_0=0, resolution='c')
m.drawcoastlines(color="#999999")
# m.fillcontinents(color='coral', lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90., 120., 30.))
m.drawmeridians(np.arange(0., 420., 60.))
# m.drawmapboundary(fill_color='aqua')

for lon in range(0, 360, 20):
    for lat in range(-60, 90, 30):
        m.tissot(lon, lat, 4, 50)

# plt.show()


###########################################################################

##########################################################################

p2 = plt.subplot(222)
my_map = Basemap(projection='robin', lat_0=0, lon_0=105,
                 resolution='l', area_thresh=1000.0)

my_map.drawparallels(np.arange(-90., 120., 30.))
my_map.drawmeridians(np.arange(0., 420., 60.))
# my_map.drawmapboundary(fill_color='aqua')
# my_map.fillcontinents(color='coral', lake_color='aqua')
my_map.drawcoastlines(color="#999999")

for lon in range(0, 360, 60):
    for lat in range(-60, 90, 30):
        my_map.tissot(lon, lat, 4, 50)

#############################################

p4 = plt.subplot(223)
my_map = Basemap(projection='cyl')

my_map.drawparallels(np.arange(-90., 120., 30.))
my_map.drawmeridians(np.arange(0., 420., 60.))
# my_map.drawmapboundary(fill_color='aqua')
# my_map.fillcontinents(color='coral', lake_color='aqua')
my_map.drawcoastlines(color="#999999")

for lon in range(0, 360, 40):
    for lat in range(-60, 90, 30):
        my_map.tissot(lon, lat, 4, 50)

#############

p3 = plt.subplot(224)
my_map = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180,
                 lat_ts=20,
                 resolution='l', )

my_map.drawparallels(np.arange(-90., 120., 30.))
my_map.drawmeridians(np.arange(0., 420., 60.))
# my_map.drawmapboundary(fill_color='aqua')
# my_map.fillcontinents(color='coral', lake_color='aqua')
my_map.drawcoastlines(color="#999999")

for lon in range(0, 360, 40):
    for lat in range(-60, 90, 30):
        my_map.tissot(lon, lat, 5, 100)

plt.savefig(get_tmp_file(__file__, '1', file_ext='png'))
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'))

plt.clf()

# plt.show()
