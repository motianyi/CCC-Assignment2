import pandas as pd
import folium
import os

states = os.path.join('data', 'us-states.json')
unemployment_data = os.path.join('data', 'US_Unemployment_Oct2012.csv')
state_data = pd.read_csv(unemployment_data)

m = folium.Map(location=[48, -102], zoom_start=3, tiles='CartoDB dark_matter')

m.choropleth(
    geo_data = states,
    name = 'choropleth',
    data = state_data,
    columns = ['State', 'Unemployment'],
    key_on = 'feature.id',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = 'Unemployment Rate %'
)

folium.LayerControl().add_to(m)

m.save('map2.html')