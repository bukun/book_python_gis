# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
con = sqlite.connect('spalite.db')
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = con.cursor()

################################################################################
sql = 'SELECT name , AsText(Geom) from pcapital limit 5'
cursor.execute(sql)
for rec in cursor: print(rec)


################################################################################
sql ='SELECT name,X(Geom),Y(Geom) FROM pcapital limit 5'
cursor.execute(sql)
for rec in cursor: print(rec)


################################################################################
sql = "SELECT HEX(GeomFromText('POINT(10 20) '));"
cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = "SELECT HEX(AsBinary(GeomFromText('POINT (10 20)')))"
cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT AsText(GeomFromWKB(
X'010100000000000000000024400000000000003440'))''' 
cursor.execute(sql)
cursor.fetchone()
