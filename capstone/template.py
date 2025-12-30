import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
from streamlit_folium import st_folium
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

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

# ---- Create severity column ----
def determine_severity(row):
    if row["fatalities_30d"] > 0:
        return "fatal"
    elif row["serious_injuries_30d"] > 0:
        return "serious"
    elif row["minor_injuries_30d"] > 0:
        return "minor"
    else:
        return "none"

df["severity"] = df.apply(determine_severity, axis=1)


# Sidebar filter by weekday
st.sidebar.header("Filter Options")
weekday_options = df["weekday"].dropna().unique()
selected_weekdays = st.sidebar.multiselect("Filter by Weekday", weekday_options, default=[])
if not selected_weekdays:
    selected_weekdays = weekday_options  # Use all if none selected

# Sidebar filter by hour
hour_options = sorted(df["hour"].dropna().unique())
selected_hours = st.sidebar.multiselect("Filter by Hour", hour_options, default=[])
if not selected_hours:
    selected_hours = hour_options  # Use all if none selected

# Sidebar filter by severity
severity_options = df["severity"].dropna().unique()
selected_severities = st.sidebar.multiselect("Filter by Severity", severity_options, default=[])
if not selected_severities:
    selected_severities = severity_options  # Use all if none selected

# Sidebar filter by month
month_options = sorted(df["month"].dropna().unique())
selected_months = st.sidebar.multiselect("Filter by Month", month_options, default=[])
if not selected_months:
    selected_months = month_options  # Use all if none selected


# Filter dataset
df_filtered = df[
    (df["weekday"].isin(selected_weekdays)) &
    (df["hour"].isin(selected_hours)) &
    (df["severity"].isin(selected_severities)) &
    (df["month"].isin(selected_months))
]


# ---- Visual summaries ----
st.subheader("Visual Summaries")

# Example 1: Accidents by severity
fig1 = px.histogram(df_filtered, x="severity", color="severity",
                    title="Accidents by Severity", 
                    labels={"severity":"Severity"}, 
                    color_discrete_sequence=px.colors.sequential.Redor)
st.plotly_chart(fig1, use_container_width=True)

# Example 2: Accidents by weekday
weekday_counts = df_filtered["weekday"].value_counts().reset_index()
weekday_counts.columns = ["weekday", "count"]  # rename columns

fig2 = px.bar(
    weekday_counts,
    x="weekday",
    y="count",
    labels={"weekday": "Weekday", "count": "Number of Accidents"},
    title="Accidents by Weekday",
    color="weekday",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
st.plotly_chart(fig2, use_container_width=True)



# ---- Insights ----
st.markdown("""
**Insights from the filtered data:**
- Most accidents occur on **{}**.
- Severity distribution shows **{}** of accidents are minor, **{}** are serious, and **{}** are fatal.
""".format(
    df_filtered["weekday"].mode()[0],
    (df_filtered["severity"]=="minor").sum(),
    (df_filtered["severity"]=="serious").sum(),
    (df_filtered["severity"]=="fatal").sum()
))





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

from folium.plugins import MarkerCluster

# Add clustering
marker_cluster = MarkerCluster().add_to(m)
for _, row in gdf.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"ID: {row['id']}<br>Severity: {row['severity']}"
    ).add_to(marker_cluster)




# Show map
st.subheader("Accident Map")
st_data = st_folium(m, width=800, height=600)
