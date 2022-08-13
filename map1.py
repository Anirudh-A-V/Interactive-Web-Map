import folium
import pandas as pd
import numpy as np
import geopandas as gpd


dams = pd.read_csv("dam.csv", encoding="latin1")
rainfall = pd.read_csv("rainfall.csv", encoding="latin1")

geoJSON_df = gpd.read_file("states.geojson")
geoJSON_df.head()

geoJSON_states = list(geoJSON_df.NAME_1.values)

no_0f_staes = len(geoJSON_states)

map = folium.Map(location=[23.036829466930804, 79.0364234261668], zoom_start=5)

folium.Choropleth(
    geo_data=geoJSON_df,
    data=geoJSON_df,
    columns=["NAME_1", "geometry"],
    key_on="feature.properties.NAME_1",
    fill_color="YlGnBu",
    fill_opacity=1,
    line_opacity=0.2,
    legend_name="wills",
    smooth_factor=0,
    Highlight=True,
    line_color="#0000",
    name="Rainfall",
    show=False,
    overlay=True,
    nan_fill_color="White",
)

# map.add_child(folium.Marker(location=[23.036829466930804, 79.0364234261668], popup="My Home", icon=folium.Icon(color='red')))

for i in range(dams.shape[0]):
    map.add_child(
        folium.Marker(
            location=[dams["Latitude"][i], dams["Longitude"][i]],
            popup=dams["dm_name"][i],
            icon=folium.Icon(color="blue"),
        )
    )

map.save("index.html")
