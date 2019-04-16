#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
con = sqlite.connect(":memory:")
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = con.cursor()
###############################################################################
cur.execute('''CREATE VIRTUAL TABLE vshp USING
  VirtualShape("/gdata/prov_capital", "UTF-8", 4326)''')
###############################################################################
cur.execute('PRAGMA table_info(vshp)')
for rec in cur: print(rec)

###############################################################################
cur.execute('''SELECT PKUID, name, lat, lon,
    AsText(Geometry) FROM vshp LIMIT 2''')
for rec in cur: print(rec)
###############################################################################
sql2 = '''SELECT PKUID, name, AsText(Geometry)
    FROM vshp WHERE lon > 105 and lat > 35 ORDER BY Name;'''
cur.execute(sql2)
for rec in cur: print(rec)

###############################################################################
cur.execute('DROP TABLE vshp')
