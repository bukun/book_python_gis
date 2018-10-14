python3 extract_py_from_latex.py
nosetests3 -v -d -s --exe part010/ch01_introduction
nosetests3 -v -d -s --exe part010/ch02_gdal
nosetests3 -v -d -s --exe part010/ch03_ogr
nosetests3 -v -d -s --exe part010/ch04_proj
nosetests3 -v -d -s --exe part010/ch05_shapely
nosetests3 -v -d -s --exe part010/ch06_spatialite
# nosetests3 -v -d -s --exe part010/ch07_mapnik
nosetests3 -v -d -s --exe part010/ch08_basemap
nosetests3 -v -d -s --exe part010/ch09_others
nosetests3 -v -d -s --exe part010/ch99_append

