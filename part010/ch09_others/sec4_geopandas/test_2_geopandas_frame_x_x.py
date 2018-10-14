# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from matplotlib import pyplot as plt
import geopandas as gpd
world = gpd.read_file('/gdata/GSHHS_c.shp')
world.head()

################################################################################
world.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()

################################################################################
world.geometry.name

################################################################################
world = world.rename(columns={'geometry': 'borders'}).set_geometry('borders')
world.geometry.name

################################################################################
world['centroid_column'] = world.centroid
world = world.set_geometry('centroid_column')
world.plot()

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()

################################################################################
