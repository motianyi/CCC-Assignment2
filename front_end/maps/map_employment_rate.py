from folium.features import Choropleth, ColorLine
import pandas as pd
import folium
import os
import numpy as np

tooltip = 'click for details'

greater_city = os.path.join('../data', 'greater_capital_city.geojson')
employment = os.path.join('../data', 'unemployment_rate.csv')
# pass total people data to city_data
employment_data = pd.read_csv(employment, usecols=np.arange(0,5))

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
        icon=folium.Icon(color='cadetblue')
    ).add_to(m)

m.choropleth(
    geo_data = greater_city,
    name = 'Employment Rate',
    data = employment_data,
    columns = [' gccsa_code_2016', ' labour_force_status_labour_force_participation_rate_pc'],
    key_on = 'feature.properties.GCC_CODE16',
    fill_color = 'YlGnBu',
    fill_opacity = 0.5,
    line_opacity = 0.2,
    legend_name = 'Employment Rate (%)',
    bins = 8,
    highlight = True
)

folium.LayerControl().add_to(m)

m.save('map_employment_rate.html')