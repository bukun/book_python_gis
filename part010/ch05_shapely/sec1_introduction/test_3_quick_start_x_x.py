#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import shapely
shapely.__version__
###############################################################################
import shapely.geos
shapely.geos.geos_version
shapely.geos.geos_capi_version
shapely.geos.geos_version_string
###############################################################################
from shapely import speedups
speedups.available
###############################################################################
speedups.disable()
speedups.enable()
