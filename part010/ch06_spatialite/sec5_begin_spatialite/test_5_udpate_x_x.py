# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import sqlite3 as sqlite
conn = sqlite.connect('/tmp/xx_new_db.sqlite')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()
recs = cur.execute("SELECT name, AsText(geom) FROM MyTable;")
for rec in recs:
    print(rec)
################################################################################
################################################################################
import sqlite3 as db
conn = db.connect('/tmp/xx_new_db.sqlite')
cur = conn.cursor()
################################################################################
del_sql = 'DELETE FROM gshhs where id > 10'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM gshhs'
res = cur.execute(sql)
for rec in res:
    print(rec)
################################################################################
del_sql = 'DELETE FROM gshhs WHERE id > 10'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM gshhs'
res = cur.execute(sql)
conn.rollback()
res = cur.execute(sql)
for rec in res:
    print(rec)
################################################################################
del_sql = 'DELETE FROM gshhs WHERE id > 10'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM gshhs'
res = cur.execute(sql)
conn.commit()
res = cur.execute(sql)
for rec in res:
    print(rec)
