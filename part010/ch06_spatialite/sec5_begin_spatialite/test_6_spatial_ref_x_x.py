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
shutil.copy("xx_china.db", tmp_db)
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
cursor = cursor.execute('SELECT DISTINCT Srid(geom) FROM gshhs;')
for rec in cursor:
    print(rec)
cursor = cursor.execute('''SELECT DISTINCT SRID(gshhs.geom), spatial_ref_sys.ref_sys_name FROM gshhs,
        spatial_ref_sys WHERE SRID(gshhs.geom) = spatial_ref_sys.srid;''')
for rec in cursor:
    print(rec)
################################################################################
cursor.execute('BEGIN')
cursor.execute("SELECT AddGeometryColumn('gshhs', 'wgs84', 4326, 'POINT', 2)")
cursor.execute("UPDATE gshhs SET wgs84 = Transform(geom, 4326);")
conn.commit()
cursor.execute('SELECT AsText(geom), Srid(geom),AsText(wgs84), \
    Srid(wgs84) FROM gshhs LIMIT 5;')
