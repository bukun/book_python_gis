#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
import sqlite3 as sqlite
con = sqlite.connect("spalite.db")
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = con.cursor()
###############################################################################
sql = '''SELECT ogc_fid, AsText(Geometry) FROM
    hyd2_4l WHERE ogc_fid = 2'''
cursor.execute(sql)
cursor.fetchone()
###############################################################################
sql = '''SELECT ogc_fid, NumPoints(Geometry),
  GLength(Geometry), Dimension(Geometry),
  GeometryType(Geometry) FROM hyd2_4l ORDER BY
  NumPoints(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
for rec in cursor: print(rec)

###############################################################################
sql = '''SELECT ogc_fid, NumPoints(Geometry),
  AsText(StartPoint(Geometry)), Y(PointN(Geometry, 2))
  FROM hyd2_4l ORDER BY NumPoints(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
for rec in cursor: print(rec)

###############################################################################
'''SELECT name, AsText(Geometry) FROM region_popu
WHERE ogc_fid = 52'''
cursor.execute(sql)
cursor.fetchone()
###############################################################################
sql='''SELECT Area(Geometry), AsText(Centroid(Geometry)),
  Dimension(Geometry), GeometryType(Geometry) FROM
  region_popu ORDER BY Area(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
for rec in cursor: print(rec)

###############################################################################
sql = '''SELECT ogc_fid, NumInteriorRings(Geometry),
    NumPoints(ExteriorRing(Geometry)),
    NumPoints(InteriorRingN(Geometry, 1))
    FROM region_popu ORDER BY NumInteriorRings(Geometry)
    DESC LIMIT 5'''
cursor.execute(sql)
for rec in cursor: print(rec)

###############################################################################
sql = '''SELECT AsText(InteriorRingN(Geometry, 1)),
    AsText(PointN(InteriorRingN(Geometry, 1), 4)),
    X(PointN(InteriorRingN(Geometry, 1), 5))
    FROM region_popu WHERE ogc_fid = 2'''
cursor.execute(sql)
cursor.fetchone()
