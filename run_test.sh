#!/usr/bin/env bash



# ogr2ogr -f SQLite -dsco SPATIALITE=YES spalite.db  /gdata/stats_county.shp -nlt polygon


# ogr2ogr -f 'SQLite' -lco SRID=4326 -nlt POINT -append spalite.db  /gdata/prov_capital.shp


python3 extract_py_from_latex.py
rm -f spalite.db

nosetests3 -v -d -s --exe part010/ch01_introduction
nosetests3 -v -d -s --exe part010/ch02_gdal
nosetests3 -v -d -s --exe part010/ch03_ogr
nosetests3 -v -d -s --exe part010/ch04_proj
nosetests3 -v -d -s --exe part010/ch05_shapely

ogr2ogr -f SQLite -dsco SPATIALITE=YES spalite.db  /gdata/county_popu.shp -nlt polygon
ogr2ogr -f 'SQLite' -lco SRID=4326 -nlt LINESTRING -append spalite.db  /gdata/hyd2_4l.shp
nosetests3 -v -d -s --exe part010/ch06_spatialite

nosetests3 -v -d -s --exe part010/ch07_mapnik
nosetests3 -v -d -s --exe part010/ch08_basemap
nosetests3 -v -d -s --exe part010/ch09_others
nosetests3 -v -d -s --exe part010/ch99_append

