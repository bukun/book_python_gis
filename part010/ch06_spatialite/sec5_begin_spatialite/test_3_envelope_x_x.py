# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import sqlite3 as sqlite
conn = sqlite.connect("xx_china.db")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()
################################################################################
sql = '''SELECT Name, AsText(Envelope(Geometry)) FROM stats_county LIMIT 5'''
cursor.execute(sql)
for x in cursor:
    print(x)
