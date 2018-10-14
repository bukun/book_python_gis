# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
db = sqlite.connect(':memory:')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = db.cursor()
cursor.execute('SELECT InitSpatialMetaData();')

################################################################################
cursor.execute("PRAGMA table_info(spatial_ref_sys)")
for rec in cursor: print(rec)


################################################################################
cursor.execute('SELECT * FROM spatial_ref_sys LIMIT 5')
for rec in cursor: print(rec)


################################################################################
import sqlite3 as sqlite
conn = sqlite.connect('spalite.db')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()
cursor.execute("select name from sqlite_master where type='table' order by name;")
for rec in cursor: print(rec)


################################################################################
cursor = cursor.execute('SELECT * FROM spatial_ref_sys LIMIT 5;')
for rec in cursor: print(rec)


################################################################################
cursor.execute('SELECT DISTINCT Srid(geom) FROM pcapital')
cursor.fetchone()
cursor.execute('''SELECT DISTINCT SRID(pcapital.geom),
    spatial_ref_sys.ref_sys_name FROM pcapital,
    spatial_ref_sys WHERE
    SRID(pcapital.geom) = spatial_ref_sys.srid;''')

cursor.fetchone()

################################################################################
cursor.execute('''SELECT AsText(Transform(geom, 3857)) from pcapital''')
cursor.fetchone()

################################################################################
cursor.execute('''SELECT AddGeometryColumn('pcapital',
    'geom3857', 3857, 'POINT', 2)''')

cursor.execute('''UPDATE pcapital SET
    geom3857 = Transform(geom, 3857)''')

cursor.execute('''SELECT AsText(geom), Srid(geom),
    AsText(geom3857), Srid(geom3857)
    FROM pcapital LIMIT 5''')

cursor.fetchone()
