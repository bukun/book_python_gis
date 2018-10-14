# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
conn = sqlite.connect('spalite.db')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

################################################################################
cursor.execute('CREATE TABLE MyTable (name TEXT NOT NULL, geom BLOB NOT NULL)')

################################################################################
cursor.execute('''INSERT INTO MyTable (name, geom) VALUES
    ('one', GeomFromText('POINT(1 1)'))''')

cursor.execute('''INSERT INTO MyTable (name, geom) VALUES
    ('two', GeomFromText('POINT(2 2)'))''')

cursor.execute('''INSERT INTO MyTable (name, geom) VALUES
    ('three', GeomFromText('POINT(3 3)'))''')

################################################################################

cursor.execute("SELECT name, AsText(geom) FROM MyTable")
for rec in cursor: print(rec)

################################################################################
cursor.execute('''SELECT id, name, AsText(geom)
    FROM pcapital where id = 32''')

for rec in cursor: print(rec)

cursor.execute('''UPDATE pcapital SET
    name='北京市', geom=GeomFromText('POINT(10 10)',
    4326)  WHERE id = 32''')

################################################################################

cursor.execute('''CREATE TABLE tab1 AS SELECT *
    FROM pcapital limit 10''')

conn.commit()

################################################################################
cursor.execute('''CREATE TABLE tab2(Name TEXT NOT NULL,
    Geometry BLOB NOT NULL)''')

cursor.execute('''INSERT INTO tab2(Name, Geometry)
    SELECT name, geom FROM pcapital limit 4''')

conn.commit()

################################################################################
cursor.execute('SELECT name, AsText(geometry) FROM tab2')
for rec in cursor: print(rec)


################################################################################
cursor.execute('DROP TABLE tab1')
cursor.execute('DROP TABLE tab2')
cursor.execute('VACUUM')
