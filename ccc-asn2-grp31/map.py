from typing import Sized
import folium
from folium.map import Tooltip
from numpy import add, tile
import os
import json
import pandas as pd
from folium.plugins import MarkerCluster

# Create a map object
m = folium.Map(location=[-37.840935, 144.946457], zoom_start=6, tiles='CartoDB dark_matter')

# add riles to map
# folium.raster_layers.TileLayer('OpenStreetMap').add_to(m)
# folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
# folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
# folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
# folium.raster_layers.TileLayer('CartoDB positron').add_to(m)
# folium.raster_layers.TileLayer('CartoDB dark_matter').add_to(m)

# # add layer control to show different maps
# folium.LayerControl(position='topright', collapsed= False).add_to(m)

# Global tootip
tooltip = 'Click For More Info'

# # Create custom marker icon
# # logoIcon = folium.features.CustomIcon('logo.jpg', icon_size=(50,50))

population = os.path.join('data', 'population.csv')
total_people = pd.read_csv(population)

# Vega data
vis = os.path.join('data', 'vis1.json')

# Geojson data
greater_city_geo = os.path.join('data', 'greater_capital_city.geojson')

# Create city markers
df = pd.DataFrame({
    'city': ['Melbourne', 'Sydney', 'Adelaide', 'Brisbane', 'Canberra', 'Perth'],
    'latitude': [-37.840935, -33.865143, -34.921230, -27.470125, -35.282001, -31.953512],
    'longitude': [144.946457, 151.209900, 138.599503, 153.021072, 149.128998, 115.857048],
})
for i, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['city'],
        tooltip=tooltip,
        icon=folium.Icon(color='beige')
    ).add_to(m)

m.choropleth(
    geo_data = greater_city_geo,
    name = 'choropleth',
    data = total_people,
    columns = ['gccsa_code_2011', 'p_tot'],
    key_on = 'feature.properties.GCC_CODE16',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = 'Number of 30-34'
)

folium.LayerControl().add_to(m)

# Create visual marker - eg
folium.Marker([-31.773512, 133.857048], 
                popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m),

# # Create a mark cluster object
# marker_cluster = MarkerCluster().add_to(m)
# for LATITUDE, LONGITUDE, ROUTES_USING_STOP in tweet_data:
#     folium.Marker(
#         location=[LATITUDE, LONGITUDE],
#         icon=None,
#         popup=ROUTES_USING_STOP,
#     ).add_to(marker_cluster)
# m.add_child(marker_cluster)

# create borders
folium.GeoJson(
    greater_city_geo,
    style_function=lambda feature: {
        'fillColor': '#B2C5B2',
        'color': '#6B8E4E',
        'weight': 2,
        'dashArray': '5,5'    
    }
).add_to(m)
# folium.GeoJson(
#     australia_geo,
#     style_function=lambda feature: {
#         'fillColor': '#B2C5B2',
#         'color': '#D5DDDF',
#         'weight': 2,
#         'dashArray': '5,5'    
#     }
# ).add_to(m)

# Generate map
m.save('map.html') 


