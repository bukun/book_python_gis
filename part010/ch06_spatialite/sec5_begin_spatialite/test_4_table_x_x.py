#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
con = sqlite.connect('spalite.db')
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = con.cursor()
###############################################################################
cursor.execute('''CREATE TABLE MyTable (name TEXT NOT NULL,
    geom BLOB NOT NULL)''')
###############################################################################
cursor.execute('''INSERT INTO MyTable (name, geom) VALUES
    ('one', GeomFromText('POINT(1 1)'))''')
cursor.execute('''INSERT INTO MyTable (name, geom) VALUES
    ('two', GeomFromText('POINT(2 2)'))''')
cursor.execute('''INSERT INTO MyTable (name, geom) VALUES
    ('three', GeomFromText('POINT(3 3)'))''')
###############################################################################
cursor.execute("SELECT name, AsText(geom) FROM MyTable")
for rec in cursor: print(rec)
###############################################################################
cursor.execute('''SELECT id, name, AsText(geom)
    FROM pcapital where id = 32''')
for rec in cursor: print(rec)

cursor.execute('''UPDATE pcapital SET
    name='北京市', geom=GeomFromText('POINT(10 10)',
    4326)  WHERE id = 32''')
###############################################################################
cursor.execute('''CREATE TABLE tab1 AS SELECT *
    FROM pcapital limit 10''')
con.commit()
###############################################################################
cursor.execute('''CREATE TABLE tab2(Name TEXT NOT NULL,
    Geometry BLOB NOT NULL)''')
cursor.execute('''INSERT INTO tab2(Name, Geometry)
    SELECT name, geom FROM pcapital limit 4''')
con.commit()
###############################################################################
cursor.execute('SELECT name, AsText(geometry) FROM tab2')
for rec in cursor: print(rec)

###############################################################################
cursor.execute('DROP TABLE tab1')
cursor.execute('DROP TABLE tab2')
cursor.execute('VACUUM')
