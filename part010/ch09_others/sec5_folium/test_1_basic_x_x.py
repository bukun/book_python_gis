# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################

################################################################################
import folium
map1 = folium.Map(location=[43.88, 125.35])
map1.save('folium_1.html')

################################################################################
map2 = folium.Map(location=[43.88, 125.35],
     tiles='Stamen Toner', zoom_start=13)

map2.save('folium_2.html')

################################################################################

################################################################################
map3 = folium.raster_layers.WmsTileLayer(
    url="http://39.107.109.21:3389/service?",
    layers="landsat2000", transparent=True, fmt="image/png",
    name="Topo4", minZoom="10")

map_wms = folium.Map(location=[43.88, 125.35], zoom_start=12,
    attr='My Data Attribution')

map3.add_to(map_wms)
map_wms.save('folium_3.html')

################################################################################
map4 = folium.Map(location=[43.92, 125.34],
    zoom_start=12, tiles='Stamen Terrain')

folium.Marker([43.852054, 125.307099], popup='长春南湖').add_to(map4)
folium.Marker([43.998071, 125.396025], popup='中科院东北地理所').add_to(map4)
map4.save('folium_4.html')

################################################################################
map5 = folium.Map(location=[43.92, 125.34], zoom_start=12, tiles='Stamen Terrain')
folium.Marker([43.852054, 125.307099], popup='长春南湖',
              icon=folium.Icon(icon='cloud')).add_to(map5)

folium.Marker([43.998071, 125.396025], popup='中科院东北地理所',
              icon=folium.Icon(color='green')).add_to(map5)

folium.Marker([43.983004, 125.356192], popup='长春北湖湿地公园',
              icon=folium.Icon(color='red')).add_to(map5)

map5.save('folium_5.html')

################################################################################
map6 = folium.Map(location=[43.92, 125.34], tiles='Stamen Toner',
                   zoom_start=12)

folium.Marker([43.852054, 125.307099], popup='长春南湖').add_to(map6)
folium.CircleMarker(location=[43.998071, 125.396025], radius=5,
                    popup='中科院东北地理所', color='#3186cc',
                    fill_color='#3186cc').add_to(map6)

map6.save('folium_6.html')

################################################################################
map7 = folium.Map(location=[43.92, 125.34], tiles='Stamen Terrain',
                   zoom_start=13)

folium.LatLngPopup().add_to(map7)
map7.save('folium_7.html')

################################################################################
map8 = folium.Map(location=[43.92, 125.34], tiles='Stamen Terrain',
                   zoom_start=12)

folium.Marker([43.852054, 125.307099], popup='长春南湖').add_to(map8)
folium.ClickForMarker(popup='Waypoint').add_to(map8)
map8.save('folium_8.html')

################################################################################
map9 = folium.Map(location=[43.92, 125.34], zoom_start=12, tiles='Stamen Terrain')
folium.RegularPolygonMarker([43.852054, 125.307099], popup='长春南湖',
    fill_color='#ff00ff', number_of_sides=4).add_to(map9)

folium.RegularPolygonMarker([43.983004, 125.356192], popup='长春北湖湿地公园',
    fill_color='#769d96', number_of_sides=6, radius=20).add_to(map9)

map9.save('folium_9.html')
