import folium
import pandas as pd

dams = pd.read_csv("Dams.csv")

map = folium.Map(location=[23.036829466930804, 79.0364234261668], zoom_start=5)

fg = folium.FeatureGroup(name="My map")
for x in dams:
    fg.add_child(folium.Marker(location=[ float(x[1]), float(x[2])], popup=x[4], icon=folium.Icon(color='blue')))
# fg.add_child(folium.Marker(location=[ 8.546818512885398, 76.90552676576516], popup="College front", icon=folium.Icon(color='blue')))
# fg.add_child(folium.Marker(location=[ 8.542525203744514, 76.90451714249187], popup="Students Shelter", icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("Map1.html")
