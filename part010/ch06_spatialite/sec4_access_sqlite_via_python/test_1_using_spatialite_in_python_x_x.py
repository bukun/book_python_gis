# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
db = sqlite.connect(':memory:')

################################################################################
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')

################################################################################
cursor = db.cursor()
cursor.execute('''select name from sqlite_master where
    type='table' order by name''')

cursor.fetchall()

################################################################################
cursor.execute('SELECT InitSpatialMetaData();')
cursor.execute('''select name from sqlite_master where
    type='table' order by name''')

cursor.fetchall()

################################################################################
cursor.execute("DROP TABLE IF EXISTS cities")
cursor.execute("CREATE TABLE cities (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "name CHAR(255))")

################################################################################

cursor.execute('''SELECT AddGeometryColumn('cities',
    'geom', 4326, 'POINT', 2)''')

################################################################################

cursor.execute("SELECT CreateSpatialIndex('cities', 'geom')")

################################################################################
cursor.execute('''INSERT INTO cities (name, geom)
   VALUES ({0}, GeomFromText({1}, 4326))'''.format(
   '"city"', '"POINT(30 40)"'))

################################################################################

cursor.execute("select name, AsText(geom) from cities")
for name,wkt in cursor: print(name, wkt)


################################################################################
cursor.execute("select name, AsText(geom) from cities")
cursor.fetchone()

################################################################################
cursor.execute("select name, AsText(geom) from cities")
all_recs = cursor.fetchall()
for name,wkt in all_recs:
    print(name, wkt)

