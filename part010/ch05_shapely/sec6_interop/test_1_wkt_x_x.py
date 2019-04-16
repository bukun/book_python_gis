#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point
Point(0, 0).wkt
Point(0, 0).wkb
###############################################################################
import codecs
codecs.encode(Point(0, 0).wkb, 'hex_codec')
###############################################################################
import binascii
binascii.hexlify(Point(0, 0).wkb)
###############################################################################
from shapely.wkb import dumps, loads
wkb = dumps(Point(0, 0))
loads(wkb).wkt
