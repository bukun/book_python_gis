#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['STKaiti']
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(6, 4))
plt.subplots_adjust(left=0.05, right=0.95, top=0.90,
    bottom=0.05, wspace=0.15, hspace=0.05)
m = Basemap(resolution='i',projection='merc',llcrnrlat=10.0,
    urcrnrlat=55.0, llcrnrlon=60., urcrnrlon=140.0)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(10., 55., 10.),labels=[1,0,0,0],
    linewidth=0.2, dashes=[4,2])
m.drawmeridians(np.arange(60., 140., 10.),labels=[0,0,0,1],
    linewidth=0.2, dashes=[4,2])
###############################################################################
x, y = m(116.42, 40.21)
x2, y2 = m(125.27, 43.83)
plt.annotate('北京', xy=(x, y), xycoords='data',
     xytext=(x2, y2), textcoords='data', color='r',
     arrowprops=dict(arrowstyle="fancy", color='g') )
plt.show()
