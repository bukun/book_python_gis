# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
world = gpd.read_file('/gdata/GSHHS_c.shp')
world['gdp_per_cap'] = world.area
world.plot(column='gdp_per_cap')

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
world.plot(column='gdp_per_cap', cmap='OrRd');

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
world.plot(column='gdp_per_cap', cmap='OrRd', scheme='quantiles');

# plt.show()

plt.savefig(get_tmp_file(__file__, '3'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '3', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
cities.plot(marker='*', color='green', markersize=5);
################################################################################
cities = cities.to_crs(world.crs)
################################################################################
base = world.plot(color='white')
cities.plot(ax=base, marker='o', color='red', markersize=5);

# plt.show()

plt.savefig(get_tmp_file(__file__, '4'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '4', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()
################################################################################
import matplotlib
matplotlib.use('Agg')
################################################################################
################################################################################
