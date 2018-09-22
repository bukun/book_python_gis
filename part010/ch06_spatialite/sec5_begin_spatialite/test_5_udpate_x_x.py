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
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
res = cur.execute(sql)
# res.next()
################################################################################
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
res = cur.execute(sql)
conn.rollback()
res = cur.execute(sql)
################################################################################
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
res = cur.execute(sql)
conn.commit()
res = cur.execute(sql)
