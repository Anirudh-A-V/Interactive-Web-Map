import folium
map = folium.Map(location=[8.546785, 76.905482])

fg = folium.FeatureGroup(name="My map")

fg.add_child(folium.Marker(location=[8.546785, 76.905482],popup="College front", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("Map1.html")