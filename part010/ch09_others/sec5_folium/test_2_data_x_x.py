# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import json
import folium
buoy_map = folium.Map(location=[46.3014, -123.7390], zoom_start=7,tiles='Stamen Terrain')
popup1 = folium.Popup(max_width=800,).add_child(
   folium.Vega( json.load(open('/gdata/folium/data/vis1.json')),
   width=500, height=250))
folium.RegularPolygonMarker([47.3489, -124.708],
   fill_color='#43d9de', radius=12, popup=popup1).add_to(buoy_map)
################################################################################
popup2 = folium.Popup(max_width=800,).add_child(
   folium.Vega(json.load(open('/gdata/folium/data/vis2.json')),
   width=500, height=250))
folium.RegularPolygonMarker([44.639, -124.5339],
   fill_color='#43d9de', radius=12, popup=popup2).add_to(buoy_map)
popup3 = folium.Popup(max_width=800,).add_child(
   folium.Vega(json.load(open('/gdata/folium/data/vis3.json')),
   width=500, height=250))
folium.RegularPolygonMarker([46.216, -124.1280],
   fill_color='#43d9de', radius=12, popup=popup3).add_to(buoy_map)
buoy_map.save('/tmp/folium_xx_NOAA_buoys.html')
################################################################################
antarctic_ice_edge = '/gdata/folium/data/antarctic_ice_edge.json'
antarctic_ice_shelf_topo = '/gdata/folium/data/antarctic_ice_shelf_topo.json'
m = folium.Map(
    location=[-59.1759, -11.6016],
    tiles='Mapbox Bright',
    zoom_start=2
)
folium.GeoJson(
    antarctic_ice_edge,
    name='geojson'
).add_to(m)
folium.TopoJson(
    open(antarctic_ice_shelf_topo),
    'objects.antarctic_ice_shelf',
    name='topojson'
).add_to(m)
folium.LayerControl().add_to(m)
m.save('/tmp/folium_xx_ice_map.html')
################################################################################
import folium
import pandas as pd
state_geo = '/gdata/folium/data/us-states.json'
state_unemployment = '/gdata/folium/data/US_Unemployment_Oct2012.csv'
state_data = pd.read_csv(state_unemployment)
m = folium.Map(location=[48, -102], zoom_start=3)
m.choropleth(geo_data=state_geo, name='choropleth', data=state_data,
    columns=['State', 'Unemployment'], key_on='feature.id',
    fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
    legend_name='Unemployment Rate (%)')
folium.LayerControl().add_to(m)
m.save('/tmp/folium_xx_us_states.html')
################################################################################
from branca.utilities import split_six
threshold_scale = split_six(state_data['Unemployment'])
m = folium.Map(location=[48, -102], zoom_start=3)
m.choropleth(geo_data=state_geo, data=state_data,columns=['State', 'Unemployment'],
    key_on='feature.id', fill_color='BuPu', fill_opacity=0.7,
    line_opacity=0.5, legend_name='Unemployment Rate (%)',
    threshold_scale=threshold_scale, reset=True)
m.save('/tmp/folium_xx_us_states_d3.html')
################################################################################
