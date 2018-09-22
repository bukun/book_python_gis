# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
################################################################################
import folium
map_osm = folium.Map(location=[45.5236, -122.6750])
map_osm.save('/tmp/folium_xx_osm.html')
################################################################################
stamen = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner', zoom_start=13)
stamen.save('/tmp/folium_xx_stamen_toner.html')
################################################################################
custom = folium.Map(location=[45.5236, -122.6750], tiles='Mapbox', API_key='the_key')
################################################################################
tileset = 'http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png'
map = folium.Map(location=[45.372, -121.6972], zoom_start=12,
           tiles=tileset, attr='My Data Attribution')
################################################################################
map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge').add_to(map_1)
map_1.save('/tmp/folium_map_pop1.html')
################################################################################
map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows',
              icon=folium.Icon(icon='cloud')).add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge',
              icon=folium.Icon(color='green')).add_to(map_1)
folium.Marker([45.3300, -121.6823], popup='Some Other Location',
              icon=folium.Icon(color='red')).add_to(map_1)
map_1.save('/tmp/folium_map_pop2.html')
################################################################################
map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',
                   zoom_start=13)
folium.Marker(location=[45.5244, -122.6699], popup='The Waterfront').add_to(map_2)
folium.CircleMarker(location=[45.5215, -122.6261], radius=500,
                    popup='Laurelhurst Park', color='#3186cc',
                    fill_color='#3186cc').add_to(map_2)
map_2.save('/tmp/folium_xx_portland.html')
################################################################################
map_3 = folium.Map(location=[46.1991, -122.1889], tiles='Stamen Terrain',
                   zoom_start=13)
folium.LatLngPopup().add_to(map_3)
map_3.save('/tmp/folium_xx_sthelens.html')
################################################################################
map_4 = folium.Map(location=[46.8527, -121.7649], tiles='Stamen Terrain',
                   zoom_start=13)
folium.Marker(location=[46.8354, -121.7325], popup='Camp Muir').add_to(map_4)
folium.ClickForMarker(popup='Waypoint').add_to(map_4)
map_4.save('/tmp/folium_xx_mtrainier.html')
################################################################################
map_5 = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.RegularPolygonMarker(location=[45.5012, -122.6655], popup='Ross Island Bridge',
    fill_color='#132b5e', number_of_sides=3, radius=10).add_to(map_5)
folium.RegularPolygonMarker(location=[45.5132, -122.6708], popup='Hawthorne Bridge',
    fill_color='#45647d', number_of_sides=4, radius=10).add_to(map_5)
folium.RegularPolygonMarker(location=[45.5275, -122.6692], popup='Steel Bridge',
    fill_color='#769d96', number_of_sides=6, radius=10).add_to(map_5)
folium.RegularPolygonMarker(location=[45.5318, -122.6745], popup='Broadway Bridge',
    fill_color='#769d96', number_of_sides=8, radius=10).add_to(map_5)
map_5.save('/tmp/folium_xx_bridges.html')
