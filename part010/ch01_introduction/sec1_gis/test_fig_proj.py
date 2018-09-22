# -*-  coding: utf-8 -*-

from helper.textool import get_tmp_file
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.clf()

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 5)

fig_index = 0

p1 = plt.subplot(121)
my_map = Basemap()
my_map.drawcoastlines()
my_map.drawmeridians(np.arange(0, 360, 60))
my_map.drawparallels(np.arange(-90, 90, 60))

p2 = plt.subplot(122)
my_map = Basemap(projection='robin', lat_0=0, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

my_map.drawcoastlines()
# my_map.drawcountries()
# my_map.fillcontinents(color='coral')
# my_map.drawmapboundary()

my_map.drawmeridians(np.arange(0, 360, 60))
my_map.drawparallels(np.arange(-90, 90, 60))

plt.savefig(get_tmp_file(__file__, '1', file_ext='png'))
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'))

plt.clf()