from folium.features import Choropleth, ColorLine
import pandas as pd
import folium
import os
import numpy as np

greater_city = os.path.join('data', 'greater_capital_city.geojson')
total_people = os.path.join('data', 'population.csv')
# pass total people data to city_data
city_data = pd.read_csv(total_people, usecols=np.arange(0,74))
# print(city_data.head(5))
# popu_dict = city_data.set_index(" gccsa_code_2011")["p_30_34_yrs"]
# print(popu_dict["1GSYD"])

m = folium.Map(location=[-37.840935, 144.946457], zoom_start=6, tiles='CartoDB dark_matter')

m.choropleth(
    geo_data = greater_city,
    name = 'choropleth',
    data = city_data,
    columns = [' gccsa_code_2011', ' p_tot'],
    key_on = 'feature.properties.GCC_CODE16',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = 'Total People',
)

folium.LayerControl().add_to(m)

m.save('map_vision.html')