from typing import Sized
import folium
from folium.map import Tooltip
from numpy import add, tile
import os
import json
import pandas as pd
from folium.plugins import MarkerCluster
import numpy as np

# Create a map object
m = folium.Map(location=[-37.840935, 144.946457], zoom_start=6)

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

# Geojson data
greater_city = os.path.join('data', 'greater_capital_city.geojson')
# csv data
total_people = os.path.join('data', 'population.csv')
# pass total people data to city_data
city_data = pd.read_csv(total_people, usecols=np.arange(0,74))

# Vega data
vis = os.path.join('data', 'vis1.json')

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
        icon=folium.Icon(color='gray')
    ).add_to(m)

# Create map division
m.choropleth(
    geo_data = greater_city,
    name = 'choropleth',
    data = city_data,
    columns = [' gccsa_code_2011', ' p_tot'],
    key_on = 'feature.properties.GCC_CODE16',
    fill_color = 'YlGnBu',
    fill_opacity = 0.8,
    line_opacity = 0.2,
    legend_name = 'Total People',
)
folium.LayerControl().add_to(m)

# Create visual marker - eg
folium.Marker([-31.773512, 133.857048], 
                popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m),

# create borders
folium.GeoJson(
    greater_city,
    style_function=lambda feature: {
        'fillColor': '#B2C5B2',
        'color': '#6B8E4E',
        'weight': 2,
        'dashArray': '5,5'    
    }
).add_to(m)

# Generate map
m.save('map.html') 


