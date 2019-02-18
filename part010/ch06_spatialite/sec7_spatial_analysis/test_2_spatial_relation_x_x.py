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
cursor.execute('''SELECT DISTINCT Srid(geom3857) FROM
    pcapital''')

cursor.fetchone()
cursor.execute('''SELECT DISTINCT Srid(geometry) FROM
    region_popu''')

cursor.fetchone()

################################################################################
sql = '''SELECT region_popu.Name FROM pcapital,
 region_popu WHERE region_popu.Name like '%市%' AND
 Within(pcapital.geom3857, region_popu.Geometry) limit 5'''

cursor.execute(sql)
for x in cursor: print(x)

for x in cursor: print(x)


################################################################################
sql = "select name from region_popu where name like '%市%' "
cursor.execute(sql)
for x in cursor: print(x)

...

################################################################################
sql = '''SELECT t2.Name,Distance(t1.geom3857,t2.geom3857)
AS Distance FROM pcapital AS t1, pcapital AS t2
WHERE t1.Name = '北京' AND
Distance(t1.geom3857, t2.geom3857) < 400000'''
cursor.execute(sql)
for x in cursor: print(x)

