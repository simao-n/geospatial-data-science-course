import geopandas as gpd
import pandas as pd
import streamlit as st
from shapely.geometry import Point

# Define data source
BASE_URL = "https://raw.githubusercontent.com/tamagusko/geospatial-data-science-course/main/data/"
FILE_NAME = "Road_Accidents_Lisbon.csv"

# Load data
df = pd.read_csv(BASE_URL + FILE_NAME)

# Convert to GeoDataFrame
df["geometry"] = [Point(xy) for xy in zip(df.longitude, df.latitude)]
gdf = gpd.GeoDataFrame(df, geometry="geometry")

# Display in Streamlit
st.title("Accident Dashboard")
st.write(gdf.head())