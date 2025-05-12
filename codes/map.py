import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Point
from streamlit_folium import st_folium

# Set page config
st.set_page_config(page_title="Lisbon Road Accidents", layout="wide")

st.title("Lisbon Road Accidents – Folium Map")
st.markdown("This dashboard uses **Folium** to visualize accident locations in Lisbon from the 2023 dataset.")



# Load data
df = pd.read_csv("data/Road_Accidents_Lisbon.csv")

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=[Point(xy) for xy in zip(df.longitude, df.latitude)],
    crs="EPSG:4326"
)

# Create base map centered on Lisbon
center = [gdf["latitude"].mean(), gdf["longitude"].mean()]
m = folium.Map(location=center, zoom_start=12, tiles="CartoDB Positron")

# Add accident points
for _, row in gdf.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=4,
        color="red",
        fill=True,
        fill_opacity=0.6,
        popup=f"ID: {row['id']}<br>Hour: {row['hour']}<br>Fatalities: {row['fatalities_30d']}"
    ).add_to(m)

# Render map in Streamlit
st_data = st_folium(m, width=800, height=600)


# Display notice
st.markdown( 
"**Important Notice:** Use is this data restricted for educational purposes within this course only."
)