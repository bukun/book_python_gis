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
shutil.copy("xx_china.db", tmp_db)
os.chmod(tmp_db, stat.S_IRUSR + stat.S_IWUSR)
conn = sqlite.connect(tmp_db)
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()
################################################################################
sql = '''SELECT stats_county.Name, COUNT(*) FROM gshhs, stats_county
 WHERE stats_county.Name IN (
 '南充市','塔河县', '伊春市', '北安市', '大庆市',
 '昌图县', '朝阳县', '顺义县', '清苑县') AND
 Within(gshhs.geom, stats_county.Geometry)
 GROUP BY stats_county.Name;'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT t2.Name,
Distance(t1.geom, t2.geom) AS Distance
FROM gshhs AS t1, gshhs AS t2
WHERE t1.Name = '北京' AND
Distance(t1.geom, t2.geom) < 10000'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
