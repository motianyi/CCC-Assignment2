from folium.features import Choropleth, ColorLine, Vega
import pandas as pd
import folium
import os
import numpy as np
from folium import IFrame

tooltip = 'click for details'

greater_city = os.path.join('../data', 'greater_capital_city.geojson')
covid = os.path.join('../data', 'covid-19.csv')
covid_data = pd.read_csv(covid, usecols=np.arange(0,5))

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
        icon=folium.Icon(color='cadetblue'),
        radius=6,
        fill_color='yellow', 
        tooltip=row['city']).add_to(m)

m.choropleth(
    geo_data = greater_city,
    name = 'covid-people',
    data = covid_data,
    columns = [' gcc_code16', ' cases'],
    key_on = 'feature.properties.GCC_CODE16',
    fill_color = 'YlOrRd',
    fill_opacity = 0.5,
    line_opacity = 0.2,
    legend_name = 'Infected Cases',
    highlight = True,
)

folium.LayerControl().add_to(m)

m.save('map_covid.html')