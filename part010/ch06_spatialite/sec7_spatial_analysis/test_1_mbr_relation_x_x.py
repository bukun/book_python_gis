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
cursor.execute("SELECT count (*) FROM county_popu;")
cursor.fetchone()

################################################################################
from shapely.geometry import box
sql = '''SELECT count(*) FROM county_popu WHERE
    MBRContains(GeomFromText('{wkt}'), geometry)'''.format(
    wkt = box(11265000,3729000,12391000,4488000).wkt)

cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT count(*) FROM county_popu WHERE
    MBRContains(BuildMBR(11265000,3729000,12391000,4488000),
    geometry)'''

cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT count (*) FROM county_popu WHERE
    MBRContains(BuildCircleMBR (11828000, 4108000, 500000),
    geometry)'''

cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT count (*) FROM county_popu WHERE
    MBRWithin( geometry , BuildMBR(
    11265000,3729000,12391000,4488000))'''

res = cursor.execute(sql)
cursor.fetchone()

################################################################################
sql = '''SELECT count (*) FROM county_popu WHERE
    MBRIntersects(BuildMBR(11265000,3729000,
    12391000,4488000), geometry)'''

cursor.execute(sql)
cursor.fetchone()
