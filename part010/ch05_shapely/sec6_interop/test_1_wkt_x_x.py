# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
from shapely.geometry import Point
Point(0, 0).wkt
Point(0, 0).wkb

################################################################################
import codecs
codecs.encode(Point(0, 0).wkb, 'hex_codec')

################################################################################
import binascii
binascii.hexlify(Point(0, 0).wkb)

################################################################################
from shapely.wkb import dumps, loads
wkb = dumps(Point(0, 0))
loads(wkb).wkt
