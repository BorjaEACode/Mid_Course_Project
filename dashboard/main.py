from folium.map import Tooltip
import streamlit as st
from data.get import get_country_list
from data.get_communities import get_ccaa_list
from data.functions import create_map, create_graph, create_table, radar_plot_ccaa
from datetime import datetime

from streamlit_folium import folium_static
import folium

st.title("Covid-19 International Dashboard")

chosen_country = st.multiselect("Select country/countries", [country["Country/Region"] for country in get_country_list()])
chosen_data = st.selectbox("Select data type", ["Cases","Deaths","Recovered"])

st.header("Data Map")

create_map(chosen_country, chosen_data)

st.header("Data Graph")
starting_date = st.date_input("Choose a starting date", value=datetime(2020,1,22),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))
ending_date = st.date_input("Choose a ending date", value=datetime(2021,4,10),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))

#create_graph(chosen_country,chosen_data,starting_date,ending_date)
#st.line_chart(data_country[0].values())

st.title("Covid-19 Spanish Dashboard")

st.header("Data Table")
chosen_ccaa = st.multiselect("Select community/communities", [ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
create_table(chosen_ccaa)

st.header("Data Radar Plot")
radar_plot = radar_plot_ccaa(chosen_ccaa)
st.plotly_chart(radar_plot)
