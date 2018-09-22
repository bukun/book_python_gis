# -*- coding: utf-8 -*-
import os
from helper.textool import get_tmp_file
import numpy as np
import matplotlib.pyplot as plot

plt = plot.subplot(111)
plt.set_xticks([])
plt.set_yticks([])

plt.spines['right'].set_color('none')
plt.spines['top'].set_color('none')
plt.spines['bottom'].set_color('none')
plt.spines['left'].set_color('none')


def get_box(x, y, d = None):

    if d:
        xx = [x + d, x + d, y + d , y + d , y]
        yy = [y, y + d , y + d , x + d , x + d]
    else:
        xx = [x, y, y, x, x]
        yy = [x, x, y, y, x]
        print('=' * 20)
        print(xx)
        print(yy)
    return (xx, yy)


color_gray = '#666666'
xx, yy = get_box(-10, 110, 2)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx, yy = get_box(-8, 112, 2)
# plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx, yy = get_box(-10, 110)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y
#######################################

xx, yy = get_box(0, 100, 2)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx, yy = get_box(2, 102, 2)
# plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx, yy = get_box(0, 100)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

#############################################################
xx, yy = get_box(12, 92, 2)
# plt.plot(xx, yy, color_gray)  # use pylab to plot x and y
xx, yy = get_box(10, 90, 2)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y
xx, yy = get_box(10, 90)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y
#################################################################
xx, yy = get_box(22, 82, 2)
# plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx, yy = get_box(20, 80, 2)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx, yy = get_box(20, 80)
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

#######################################################################

xx = [30, 70, 70, 30, 30]
yy = [30, 30, 45, 45, 30]
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

xx = [30, 70, 70, 30, 30]
yy = [55, 55, 70, 70, 55]
plt.plot(xx, yy, color_gray)  # use pylab to plot x and y

plt.text(-8, 105, 'Map')
plt.text(2, 95, 'Layer')
plt.text(12, 85, 'Style')
plt.text(22, 75, 'Rule')
plt.text(32, 65, 'Filter (optional)')
plt.text(32, 40, 'Symbolizer')
# plt.show()  # show the plot on the screen


plot.savefig(get_tmp_file(__file__))
plot.savefig(get_tmp_file(__file__, file_ext='pdf'))