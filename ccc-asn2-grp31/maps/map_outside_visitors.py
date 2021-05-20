from folium.features import Choropleth, ColorLine
import pandas as pd
import folium
import os
import numpy as np

tooltip = 'click for details'

greater_city = os.path.join('../data', 'greater_capital_city.geojson')
total_people = os.path.join('../data', 'population.csv')
# pass total people data to city_data
p_data = pd.read_csv(total_people, usecols=np.arange(0,3))

m = folium.Map(location=[-35.282001, 149.128998], zoom_start=6)

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

m.choropleth(
    geo_data = greater_city,
    name = 'Outside Visitors',
    data = p_data,
    columns = ['gcc_code16', ' os_vis_p'],
    key_on = 'feature.properties.GCC_CODE16',
    fill_color = 'RdPu',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = 'Outside Visitors',
    bins = 8,
    highlight = True
)

folium.LayerControl().add_to(m)

m.save('map_outside_visitors.html')