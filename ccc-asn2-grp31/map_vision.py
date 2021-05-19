from folium.features import Choropleth
import pandas as pd
import folium
import os

greater_city = os.path.join('data', 'greater_capital_city.json')
total_people = os.path.join('ccc-asn2-grp31','data', 'population.csv')
# pass total people data to city_data
city_data = pd.read_csv(total_people, usecols=[0,71])
# 这里都可以显示出前5排，第1列和第72列的数据
print(city_data.head(5))
popu_dict = city_data.set_index("gccsa_code_2011")["p_30_34_yrs"]
# 从这里开始就显示找不到csv里面的gccsa_code_2011，但是csv里面这组数据在倒数第4列
# print(popu_dict["1GSYD"])

# m.choropleth(
#     geo_data = greater_city,
#     name = 'choropleth',
#     data = city_data,
#     columns = ['gccsa_code_2011', 'p_tot'],
#     key_on = 'feature.properties.GCC_CODE16',
#     fill_color = 'YlGn',
#     fill_opacity = 0.7,
#     line_opacity = 0.2,
#     legend_name = 'Total people'
# )

# folium.LayerControl().add_to(m)

# m.save('map_vision.html')