# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

################################################################################
bsmap = Basemap()

################################################################################
bsmap.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '1'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '1', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()

################################################################################
plt.savefig('xx_test.png')

################################################################################
bsmap = Basemap(projection='ortho',lat_0=0, lon_0=105)
bsmap.drawmapboundary(fill_color='aqua')

################################################################################
bsmap.fillcontinents(color= 'coral',lake_color='aqua')
bsmap.drawcoastlines()

# plt.show()

plt.savefig(get_tmp_file(__file__, '2'), bbox_inches='tight', dpi=600)
plt.savefig(get_tmp_file(__file__, '2', file_ext='pdf'), bbox_inches='tight', dpi=600)
plt.clf()

################################################################################
plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window
