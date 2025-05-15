import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
from streamlit_folium import st_folium

# Page configuration
st.set_page_config(page_title="Lisbon Road Accidents", layout="wide")

# Title and description
st.title("Lisbon Road Accidents – Interactive Dashboard")
st.markdown(
    "Explore and analyze road accident data from Lisbon."
)

# Educational use notice
st.markdown(
    """
> ⚠️ **Important Notice**  
> This dataset contains real road accident records from Portugal in 2023, provided by **ANSR (National Road Safety Authority)**.  
> It is intended **exclusively for educational use within this course**. Redistribution or use for any other purpose is strictly prohibited.
"""
)

# Load dataset
df = pd.read_csv("data/Road_Accidents_Lisbon.csv")

# Sidebar filter by weekday
st.sidebar.header("Filter Options")
weekday_options = df["weekday"].dropna().unique()
selected_weekdays = st.sidebar.multiselect("Filter by Weekday", weekday_options, default=weekday_options)

# Filter dataset
df_filtered = df[df["weekday"].isin(selected_weekdays)]

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df_filtered,
    geometry=[Point(xy) for xy in zip(df_filtered["longitude"], df_filtered["latitude"])],
    crs="EPSG:4326"
)

# Center map on Lisbon
center = [gdf["latitude"].mean(), gdf["longitude"].mean()]
m = folium.Map(location=center, zoom_start=12, tiles="CartoDB Positron")

# Add accident markers
for _, row in gdf.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5,
        color="red",
        fill=True,
        fill_opacity=0.6,
        popup=f"ID: {row['id']}<br>Weekday: {row['weekday']}<br>Fatalities: {row['fatalities_30d']}"
    ).add_to(m)

# Show map
st.subheader("Accident Map")
st_data = st_folium(m, width=800, height=600)
