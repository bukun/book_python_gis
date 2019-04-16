#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
dbfile = 'spalite.db'
###############################################################################
con = sqlite.connect(dbfile)
con.enable_load_extension(True)
con.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = con.cursor()
###############################################################################
cursor.execute("DROP TABLE IF EXISTS pcapital")
cursor.execute('''CREATE TABLE pcapital (id INTEGER PRIMARY
    KEY AUTOINCREMENT,name varchar(100))''')
cursor.execute('''CREATE INDEX pcapital_name on
    pcapital(name)''')
cursor.execute('''SELECT AddGeometryColumn('pcapital',
    'geom', 4326, 'POINT', 2)''')
cursor.execute("SELECT CreateSpatialIndex('pcapital', 'geom')")
con.commit()
###############################################################################
from osgeo import ogr
fName = '/gdata/prov_capital.shp'
shapefile = ogr.Open(fName)
layer = shapefile.GetLayer(0)
###############################################################################
sql_tpl = '''INSERT INTO pcapital (name, geom) VALUES
    ('{0}', GeomFromText('{1}', 4326))'''
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    fd_name = feature.GetField('name')
    geometry = feature.GetGeometryRef()
    wkt = geometry.ExportToWkt()
    cursor.execute( sql_tpl.format(fd_name ,wkt))
con.commit()
