#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import folium; import json
map_a = folium.Map(location=[46.3014, -123.7390],
    zoom_start=7,tiles='Stamen Terrain')
popup1 = folium.Popup(max_width=800,).add_child(
    folium.Vega(
        json.load(open('/gdata/folium/data/vis1.json')),
        width=500, height=250))
folium.RegularPolygonMarker([47.3489, -124.708],
   fill_color='#ff0000', radius=12, popup=popup1
    ).add_to(map_a)
###############################################################################
popup2 = folium.Popup(max_width=800,).add_child(
    folium.Vega(
        json.load(open('/gdata/folium/data/vis2.json')),
        width=500, height=250))
folium.RegularPolygonMarker([44.639, -124.5339],
    fill_color='#00ff00', radius=12, popup=popup2
    ).add_to(map_a)
###############################################################################
popup3 = folium.Popup(max_width=800,).add_child(
    folium.Vega(
        json.load(open('/gdata/folium/data/vis3.json')),
        width=500, height=250))
folium.RegularPolygonMarker([46.216, -124.1280],
    fill_color='#0000ff', radius=12, popup=popup3
    ).add_to(map_a)
map_a.save('folium_a.html')
###############################################################################
ice_edge = '/gdata/folium/data/antarctic_ice_edge.json'
map_b = folium.Map(
    location=[-59.1759, -11.6016],
    tiles='Mapbox Bright',
    zoom_start=2
)
folium.GeoJson(ice_edge, name='geojson').add_to(map_b)
###############################################################################
icej='/gdata/folium/data/antarctic_ice_shelf_topo.json'
folium.TopoJson(open(icej),
    'objects.antarctic_ice_shelf',
    name='topojson'
).add_to(map_b)
###############################################################################
folium.LayerControl().add_to(map_b)
map_b.save('folium_b.html')
###############################################################################
import pandas as pd
state_geo = '/gdata/folium/data/us-states.json'
csvf = '/gdata/folium/data/US_Unemployment_Oct2012.csv'
state_data = pd.read_csv(csvf)
map_c = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=state_geo,
    name='choropleth', data=state_data,
    columns=['State', 'Unemployment'], key_on='feature.id',
    fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
    legend_name='失业率 (%)').add_to(map_c)
folium.LayerControl().add_to(map_c)
map_c.save('folium_c.html')
###############################################################################
bins = list(state_data['Unemployment'].quantile([0,0.25,0.5,0.75,1]))
map_d = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=state_geo, data=state_data,
    columns=['State', 'Unemployment'], key_on='feature.id',
    fill_color='BuPu', fill_opacity=0.7,
    line_opacity=0.5, legend_name='失业率 (%)',
    bins=bins, reset=True).add_to(map_d)
map_d.save('folium_d.html')
