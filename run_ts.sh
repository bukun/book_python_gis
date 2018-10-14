#!/usr/bin/env bash

python3 extract_py_from_latex.py

rm -f spalite.db
ogr2ogr -f SQLite -dsco SPATIALITE=YES spalite.db  /gdata/county_popu.shp -nlt polygon
ogr2ogr -f 'SQLite' -lco SRID=4326 -nlt LINESTRING -append spalite.db  /gdata/hyd2_4l.shp

nosetests3 -v -d -s --exe ./part010/ch06_spatialite/sec4_access_sqlite_via_python/



nosetests3 -v -d -s --exe ./part010/ch06_spatialite/


