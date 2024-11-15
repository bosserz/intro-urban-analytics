import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

# Load CSV data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


# Streamlit App
st.title("Spatiotemperal Analysis of Imbalanced Parking Demand and Supply")

# 1) Objective
st.header("Objective of the Project")
st.write("Describe the objective of the project here.")

# 2) Data
st.header("Data")
st.write("Brief description of the data being used.")

# 3) Methodology
st.header("Methodology")
st.write("Describe methodology use in the project.")

# 4) Results
st.header("Results")
st.subheader("Maps")
data = load_data("./data/parking_demand_supply.csv")
# st_folium(map_data, width=700, height=500)
fig = px.scatter_mapbox(
    data,
    lat="LATITUDE",
    lon="LONGITUDE",
    # size="value", 
    color="sum_k2",  # Column representing demand
    hover_name="park_key",  # Column to show on hover
    color_continuous_scale="Viridis",  # Choose a color scale
    zoom=8,
    mapbox_style="carto-positron"
)
st.plotly_chart(fig, use_container_width=True)


# 5) Conclusion
st.header("Conclusion")
st.write("Summarize the findings and conclusions here.")

st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate to different sections of the app.")

sections = ["Objective", "Data", "Methodology", "Results", "Conclusion"]
selected_section = st.sidebar.radio("Navigate to Section:", sections)

# Sections
if selected_section == "Objective":
    st.header("Objective of the Project")
    st.write("Describe the objective of your project here.")
    
elif selected_section == "Data":
    st.header("Data")
    st.write("Upload and explore your data here.")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        data = load_data(uploaded_file)
        st.write(data.head())

elif selected_section == "Methodology":
    st.header("Methodology")
    st.write("Describe the methodology used in your project here.")

elif selected_section == "Results":
    st.header("Results")
    st.subheader("Bubble Map with Demand-Based Colors")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="results_file")
    if uploaded_file:
        data = load_data(uploaded_file)
        bubble_map = plot_bubble_map(data)
        st_folium(bubble_map, width=700, height=500)

    st.subheader("Graphs")
    st.write("Add graphs here for further insights.")

elif selected_section == "Conclusion":
    st.header("Conclusion")
    st.write("Summarize the findings and conclusions of your project.")

# Sidebar Note
st.sidebar.write("---")
st.sidebar.write("Use the sidebar to navigate between sections.")