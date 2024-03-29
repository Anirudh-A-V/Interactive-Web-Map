import folium
import pandas as pd

dams = pd.read_csv("./data/dam.csv", encoding="latin1")

map = folium.Map(location=[23.036829466930804, 79.0364234261668], zoom_start=5)

for i in range(dams.shape[0]):
    map.add_child(
        folium.Marker(
            location=[dams["Latitude"][i], dams["Longitude"][i]],
            popup=dams["dm_name"][i],
            icon=folium.Icon(color="blue"),
        )
    )

map.save("index.html")

