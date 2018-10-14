# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as db
conn = db.connect('spalite.db')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()

################################################################################
sql_count = 'SELECT count(*) FROM pcapital'
cur.execute(sql_count).fetchone()

################################################################################
del_sql = 'DELETE FROM pcapital where id > 10'
cur.execute(del_sql)
cur.execute(sql_count).fetchone()

################################################################################
conn.rollback()
cur.execute(sql_count).fetchone()

################################################################################
cur.execute(del_sql)
conn.commit()

################################################################################
conn.rollback()
cur.execute(sql_count).fetchone()
conn.close()
