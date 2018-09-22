# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import os; import sqlite3 as sqlite
dbfile = '/tmp/xx_shapedb.sqlite'
if os.path.exists(dbfile): os.remove(dbfile)
################################################################################
db = sqlite.connect(dbfile)
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = db.cursor()
cursor.execute('SELECT InitSpatialMetaData();')
################################################################################
cursor.execute("DROP TABLE IF EXISTS gshhs")
cursor.execute("CREATE TABLE gshhs (" +
"id INTEGER PRIMARY KEY AUTOINCREMENT, " +
"level INTEGER)")
cursor.execute("CREATE INDEX gshhs_level on gshhs(level)")
cursor.execute("SELECT AddGeometryColumn('gshhs', 'geom', " +
"4326, 'POLYGON', 2)")
cursor.execute("SELECT CreateSpatialIndex('gshhs', 'geom')")
db.commit()
################################################################################
import ogr
fName = '/gdata/GSHHS_c.shp'
shapefile = ogr.Open(fName)
layer = shapefile.GetLayer(0)
################################################################################
sql_tpl = "INSERT INTO gshhs (level, geom) VALUES (2, GeomFromText('{0}', 4326))"
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    geometry = feature.GetGeometryRef()
    wkt = geometry.ExportToWkt()
    cursor.execute( sql_tpl.format(wkt))

db.commit()
