#!/usr/bin/env bash
python3 extract_py_from_latex.py
# nosetests3  --exe -v -d -s part010/ch07_mapnik/
#nosetests3 -v -d -s --exe part010/ch09_others/sec5_folium/
#cp -r folium_*.html /opt/tmp/


# nosetests3 -v -d -s --exe part010/ch05_shapely/sec4_spatial_analysis
# nosetests3 -v -d -s --exe part010/ch08_basemap

nosetests3 -v -d -s --exe part010/ch08_basemap/sec4_example/
