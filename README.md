# Geospatial Data Science for Urban Mobility

This repository contains Jupyter Notebooks developed for the **Geospatial Data Science for Urban Mobility** course. These notebooks provide hands-on examples for analyzing and visualizing mobility patterns using Python and geospatial tools like `GeoPandas`, `OSMnx`, `Folium`, `Contextily`, and others.

## 📘 Course Modules and Notebooks

Each module below contains notebooks with practical examples and exercises.

---

### ✅ Module 1 – Foundations of Urban Mobility
*No notebook – theoretical introduction*

---

### 📂 Module 2 – Mobility Data Sources & Open Data

- [module_2_episode_8_osm_intro.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/module_2_episode_8_osm_intro.ipynb)

---

### 📂 Module 3 – Geospatial Data Foundations

- [module_3_episode_11_geopandas_intro.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/module_3_episode_11_geopandas_intro.ipynb)  
- [module_3_episode_12_walk_route.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/module_3_episode_12_walk_route.ipynb)

---

### 📂 Module 4 – Data Preparation & Feature Engineering

- [module_4_episode_15_cleaning.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/module_4_episode_15_cleaning.ipynb)

---

### 📂 Module 5 – Visualizing Urban Mobility

- [Module_5_Episode_18_Accident_Map.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/Module_5_Episode_18_Accident_Map.ipynb)

---

### 📂 Module 6 – Spatial Analysis

- [Module_6_Episode_19_Folium_Accidents.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/Module_6_Episode_19_Folium_Accidents.ipynb)  
- [module_6_episode_22_isochrones.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/module_6_episode_22_isochrones.ipynb)  
- [Module_6_Episode_23_DBSCAN_Hotspot_Map.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/Module_6_Episode_23_DBSCAN_Hotspot_Map.ipynb)

---

### 📂 Module 7 – Hands-On: Road Accident Analysis

- [Module_7_Episode_26_Road_Accident_Analysis.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/Module_7_Episode_26_Road_Accident_Analysis.ipynb)  
- [Modulo_7_episode_27_Heatmap.ipynb](https://colab.research.google.com/github/tamagusko/geospatial-data-science-course/blob/main/notebooks/Modulo_7_episode_27_Heatmap.ipynb)

---

## 🚀 How to Use

### 1. Open in Google Colab (Recommended)

Just click any notebook link above to launch it in Colab—no installation needed. This is the easiest and most beginner-friendly way to follow the course.

### 2. Run Locally

If you prefer to run notebooks on your machine:

```
# Clone the repository
git clone https://github.com/tamagusko/geospatial-data-science-course.git
cd geospatial-data-science-course

# Install required dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
````

---

## 🧭 Streamlit for Dashboards

Some modules include the use of `Streamlit` to build simple interactive dashboards using geospatial data and maps.

To get started with Streamlit:

1. Install Streamlit and dependencies:

```
pip install streamlit folium streamlit-folium geopandas shapely pandas
```

2. Run a dashboard example:

```
streamlit run codes/map.py
```

📚 Official docs: [https://docs.streamlit.io/get-started](https://docs.streamlit.io/get-started)
