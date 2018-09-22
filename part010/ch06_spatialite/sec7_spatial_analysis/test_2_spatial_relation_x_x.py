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
sql = '''SELECT Regions.Name, COUNT(*) FROM Towns, Regions
 WHERE Regions.Name IN (
 'VALLED','AOSTA', 'PIEMONTE', 'UMBRIA', 'LOMBARDIA',
 'CALABRIA', 'MOLISE', 'MARCHE', 'BASILICATA') AND
 Within(Towns.geometry, Regions.Geometry)
 GROUP BY Regions.Name;'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT t2.Name, t2.Peoples,
Distance(t1.geometry, t2.geometry) AS Distance
FROM Towns AS t1, Towns AS t2
WHERE t1.Name = 'Firenze' AND
Distance(t1.geometry, t2.geometry) < 10000'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
