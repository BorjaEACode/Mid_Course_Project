from folium.map import Tooltip
import streamlit as st
from data.get import get_country_list, get_country_data, get_country_coord
from data.functions import create_map, create_coord_list, create_data_list
from datetime import datetime

from streamlit_folium import folium_static
import folium

st.title("Covid-19 International Dashboard")
st.header("This is a streamlit display for visualizing data about Covid-19 on international scope")

chosen_country = st.multiselect("Select country", [country["Country/Region"] for country in get_country_list()])
chosen_data = st.selectbox("Select data type", ["Cases","Deaths","Recovered"])

st.text("")
#st.text("Its coordinates are: ")
#st.text(coord_country)

st.text("")
#st.text("Its data is: ")
#st.text(data_country)
st.date_input("Choose a date", value=datetime(2021,4,10),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))
st.header("Data Graph")
st.text("")


#st.line_chart(data_country[0].values())

st.header("Data Map")
st.text("")

create_map(chosen_country, chosen_data)

