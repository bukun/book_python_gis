# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import sqlite3 as sqlite
conn = sqlite.connect("/gdata/test-2.3.sqlite")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()
################################################################################
sql = '''SELECT name , peoples , AsText(Geometry) from Towns
    where peoples > 350000 order by peoples DESC'''
cursor.execute(sql)
for x in cursor:
    print(x)
################################################################################
sql = 'SELECT name , X(Geometry), Y(Geometry) FROM Towns WHERE peoples > 350000 ORDER BY peoples DESC;'
cursor.execute(sql)
for x in cursor:
    print(x)
################################################################################
sql = "SELECT HEX(GeomFromText('POINT(10 20) '));"
cursor.execute(sql)
for rec in cursor:
    print(rec)
sql = "SELECT HEX(AsBinary(GeomFromText('POINT(10 20) ')));"
cursor.execute(sql)
for rec in cursor:
    print(rec)
sql = "SELECT AsText(GeomFromWKB(X'010100000000000000000024400000000000003440'));"
cursor.execute(sql)
for rec in cursor:
    print(rec)
