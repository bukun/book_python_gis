#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import geopandas as gpd
import matplotlib.pyplot as plt
world = gpd.read_file('/gdata/GSHHS_c.shp')
world['gdp_per_cap'] = world.area
world.plot(column='gdp_per_cap')
plt.show()
###############################################################################
world.plot(column='gdp_per_cap', cmap='OrRd');
plt.show()
###############################################################################
world.plot(column='gdp_per_cap', cmap='OrRd',
    scheme='quantiles')
plt.show()
###############################################################################
cities = gpd.read_file(gpd.datasets.get_path(
    'naturalearth_cities'))
cities.plot(marker='*', color='green', markersize=5)
###############################################################################
cities = cities.to_crs(world.crs)
###############################################################################
base = world.plot(color='white')
cities.plot(ax=base, marker='o',color='red',markersize=5)
plt.show()
