# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import sqlite3 as sqlite
db = sqlite.connect(':memory:')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = db.cursor()
cursor.execute('SELECT InitSpatialMetaData();')
################################################################################
for rec in cursor.execute("PRAGMA table_info(spatial_ref_sys)"):
    print(rec)

################################################################################
for rec in cursor.execute('SELECT * FROM spatial_ref_sys LIMIT 5;'):
    print(rec)

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
cursor.execute("select name from sqlite_master where type='table' order by name;")
for rec in cursor:
    print(rec)
################################################################################
cursor = cursor.execute('SELECT * FROM spatial_ref_sys LIMIT 5;')
for rec in cursor:
    print(rec)
################################################################################
cursor = cursor.execute('SELECT DISTINCT Srid(geometry) FROM Towns;')
for rec in cursor:
    print(rec)
cursor = cursor.execute('''SELECT DISTINCT SRID(Towns.geometry), spatial_ref_sys.ref_sys_name FROM Towns,
        spatial_ref_sys WHERE SRID(Towns.geometry) = spatial_ref_sys.srid;''')
for rec in cursor:
    print(rec)
################################################################################
cursor.execute('BEGIN')
cursor.execute("SELECT AddGeometryColumn('Towns', 'wgs84', 4326, 'POINT', 2)")
cursor.execute("UPDATE Towns SET wgs84 = Transform(geometry, 4326);")
conn.commit()
cursor.execute('SELECT AsText(geometry), Srid(geometry),AsText(wgs84), \
    Srid(wgs84) FROM Towns LIMIT 5;')
