#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from matplotlib import pyplot as plt
import geopandas as gpd
world = gpd.read_file('/gdata/GSHHS_c.shp')
world.head()
###############################################################################
world.plot()
plt.show()
###############################################################################
world.geometry.name
###############################################################################
world = world.rename(columns={'geometry': 'borders'}
    ).set_geometry('borders')
world.geometry.name
###############################################################################
world['centroid_column'] = world.centroid
world = world.set_geometry('centroid_column')
world.plot()
plt.show()
