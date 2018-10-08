# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import os,shutil,stat
import sqlite3 as sqlite
tmp_db = '/tmp/xx_new_db.sqlite'
if os.path.exists(tmp_db):
    os.remove(tmp_db)
shutil.copy("/gdata/test-2.3.sqlite", tmp_db)
os.chmod(tmp_db, stat.S_IRUSR + stat.S_IWUSR)
conn = sqlite.connect(tmp_db)
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
for rec in cursor:
    print(rec)
################################################################################
cursor.execute('''SELECT pk_uid, name, peoples, 
    AsText(geometry) FROM Towns WHERE pk_uid = 8006")
for rec in cursor:
    print(rec)
cursor.execute('''UPDATE Towns SET peoples = 150000,
    name='MONZA', geometry=GeomFromText('POINT(10 10)',
    32632)  WHERE pk_uid = 8006''')
cursor.execute('''SELECT pk_uid, name, peoples, 
    AsText(geometry) FROM Towns WHERE pk_uid = 8006''')
for rec in cursor:
    print(rec)
################################################################################
cursor.execute('CREATE TABLE Villages AS SELECT * FROM Towns WHERE peoples < 500')
conn.commit()
################################################################################
cursor.execute('CREATE TABLE Metropolis ( Name TEXT NOT NULL, Population INTEGER NOT NULL, Geometry BLOB NOT NULL);')
cursor.execute('''INSERT INTO Metropolis (Name, Population, Geometry)
        SELECT name, peoples, geometry FROM Towns
        WHERE peoples > 1000000;''')
conn.commit()
cursor.execute('SELECT name, population, AsText(geometry) FROM Metropolis')
################################################################################
cursor.execute('DROP TABLE Villages')
cursor.execute('DROP TABLE Metropolis')
cursor.execute('VACUUM')
