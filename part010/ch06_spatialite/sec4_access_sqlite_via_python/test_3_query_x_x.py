# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import sqlite3 as sqlite
# db = sqlite.connect('/tmp/xx_shapedb.sqlite')
db = sqlite.connect('xx_china.db')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = db.cursor()
################################################################################
import shapely.wkt

Beijing = 'POINT(116.0676 39.8919 )'
pt = shapely.wkt.loads(Beijing)

cursor.execute("SELECT id,level,AsText(geom) " +
     "FROM gshhs WHERE id IN " +
     "(SELECT pkid FROM idx_gshhs_geom" +
     " WHERE round(xmin,4) <= ? AND ? <= round(xmax,4)" +
     " AND round(ymin,4) <= ? and ? <= round(ymax,4)) " +
     "AND Contains(round(geom,4), GeomFromText(?, 4326))",
     (pt.x, pt.x, pt.y, pt.y, Beijing))
shoreline = None
for id, level, wkt in cursor:
    shoreline = wkt
################################################################################
with open("xxz_uk-shoreline.wkt", "w") as fout:
    if shoreline:
        fout.write(shoreline)
################################################################################
cursor.execute("EXPLAIN QUERY PLAN " +
    "SELECT id,level,AsText(geom) " +
    "FROM gshhs WHERE id IN " +
    "(SELECT pkid FROM idx_gshhs_geom" +
    " WHERE xmin <= ? AND ? <= xmax" +
    " AND ymin <= ? and ? <= ymax) " +
    "AND Contains(geom, GeomFromText(?, 4326))",
    (pt.x, pt.x, pt.y, pt.y, Beijing))
################################################################################
for row in cursor:
    print (row)

