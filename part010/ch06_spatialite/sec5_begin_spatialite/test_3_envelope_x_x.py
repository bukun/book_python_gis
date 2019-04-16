#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
con = sqlite.connect('spalite.db')
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = con.cursor()
###############################################################################
sql = '''SELECT Name, AsText(Envelope(Geometry)) FROM
  region_popu  LIMIT 5'''
cursor.execute(sql)
for x in cursor: print(x)

