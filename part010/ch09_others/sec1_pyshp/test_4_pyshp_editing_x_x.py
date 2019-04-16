#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import shapefile
e = shapefile.Editor(shapefile="xx_sf_point.shp")
###############################################################################
e.point(0,0,10,2)
e.record("Appended","Point")
e.save('xx_sf_point')
###############################################################################
e = shapefile.Editor(shapefile="xx_sf_line.shp")
e.line(parts=[[[10,5],[15,5],[15,1],[13,3],[11,1]]])
e.record('Appended','Line')
e.save('xx_sf_line')
###############################################################################
e = shapefile.Editor(shapefile="xx_sf_polygon.shp")
e.poly(parts=[[[5.1,5],[9.9,5],[9.9,1],[7.5,3],[5.1,1]]])
e.record("Appended","Polygon")
e.save('xx_sf_polygon')
###############################################################################
e = shapefile.Editor(shapefile="xx_sf_point.shp")
e.delete(0)
e.save('xx_sf_point')
###############################################################################
e = shapefile.Editor(shapefile="xx_sf_polygon.shp")
e.delete(-1)
e.save('xx_sf_polygon')
