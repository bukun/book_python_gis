# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
con = sqlite.connect('spalite.db')
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = con.cursor()

################################################################################
sql_count = 'SELECT count(*) FROM pcapital'
cur.execute(sql_count).fetchone()

################################################################################
del_sql = 'DELETE FROM pcapital where id > 10'
cur.execute(del_sql)
cur.execute(sql_count).fetchone()

################################################################################
con.rollback()
cur.execute(sql_count).fetchone()

################################################################################
cur.execute(del_sql)
con.commit()

################################################################################
con.rollback()
cur.execute(sql_count).fetchone()
con.close()
