# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import sqlite3 as sqlite
db = sqlite.connect('spalite.db')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = db.cursor()

################################################################################
cursor.execute('''SELECT name, AsText(geom)
FROM pcapital WHERE id IN
(SELECT pkid FROM idx_pcapital_geom
WHERE xmin >= 90 AND xmax <= 110
AND ymin >= 30 and ymax<= 40)''')
for row in cursor: print (row)


################################################################################
from shapely.geometry import box
cursor.execute('''SELECT name, AsText(geom) FROM
pcapital WHERE Contains(GeomFromText("{wkt}", 4326), geom)
'''.format(wkt = box(90,30,110,40).wkt))

################################################################################
for row in cursor: print (row)

