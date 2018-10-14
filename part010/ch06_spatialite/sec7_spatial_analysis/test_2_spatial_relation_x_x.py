# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
conn = sqlite.connect('spalite.db')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

################################################################################
cursor = cursor.execute('SELECT DISTINCT Srid(geom3857) FROM pcapital')
cursor.fetchone()
cursor = cursor.execute('SELECT DISTINCT Srid(geometry) FROM county_popu')
cursor.fetchone()

################################################################################
sql = '''SELECT county_popu.Name FROM pcapital,
 county_popu WHERE county_popu.Name like '%长%' AND
 Within(pcapital.geom3857, county_popu.Geometry)'''

cursor.execute(sql)
for x in cursor: print(x)


################################################################################
sql = "select name from county_popu where name like '%长%' "
cursor.execute(sql)
for x in cursor: print(x)



################################################################################
sql = '''SELECT t2.Name,Distance(t1.geom3857,t2.geom3857)
AS Distance FROM pcapital AS t1, pcapital AS t2
WHERE t1.Name = '北京' AND
Distance(t1.geom3857, t2.geom3857) < 400000'''
cursor.execute(sql)
for x in cursor: print(x)

