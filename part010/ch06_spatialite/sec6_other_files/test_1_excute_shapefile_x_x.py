# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import os, sys, stat
import shutil
import sqlite3 as sqlite
sqlite_file = '/tmp/xx_new_db.sqlite'
if os.path.exists(sqlite_file):
    os.remove(sqlite_file)
shutil.copy("/gdata/test-2.3.sqlite", sqlite_file)
os.chmod(sqlite_file, stat.S_IRUSR + stat.S_IWUSR)
conn = sqlite.connect(sqlite_file)
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()
################################################################################
sql = 'CREATE VIRTUAL TABLE uu USING VirtualShape("/gdata/prov_capital", "UTF-8", 4326)'
cur.execute(sql)
################################################################################
cur.execute('PRAGMA table_info(uu)')
for rec in cur:
    print(rec)

################################################################################
cur.execute('SELECT PKUID, name, lat, lon, AsText(Geometry) FROM uu LIMIT 2')
for rec in cur:
    print(rec)
################################################################################
sql2 = '''SELECT PKUID, name, AsText(Geometry)
    FROM uu WHERE lon > 105 and lat > 35 ORDER BY Name;'''
cur.execute(sql2)
for rec in cur:
    print(rec)

################################################################################
cur.execute('DROP TABLE uu')
