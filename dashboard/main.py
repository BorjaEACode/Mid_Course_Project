from folium.map import Tooltip
import streamlit as st
from data.get import get_country_list, get_country_data, get_country_coord

from streamlit_folium import folium_static
import folium
import pandas as pd

st.title("Covid-19 International Dashboard")
st.header("This is a streamlit display for visualizing data about Covid-19 on international scope")

chosen_country = st.selectbox("Select country", [country["Country/Region"] for country in get_country_list()])
chosen_data = st.selectbox("Select data type", ["Cases","Deaths","Recovered"])

data_country = get_country_data(chosen_country, chosen_data)
coord_country = get_country_coord(chosen_country)

st.text("")
#st.text("Its coordinates are: ")
#st.text(coord_country)

st.text("")
#st.text("Its data is: ")
#st.text(data_country)

st.header("Data Graph")
st.text("")


st.line_chart(data_country[0].values())

st.header("Data Map")
st.text("")

m = folium.Map(location=(coord_country[0]["Lat"],coord_country[0]["Long"]), zoom_start=4)
folium.Marker((coord_country[0]["Lat"],coord_country[0]["Long"]), popup=chosen_country, tooltip=(chosen_country,data_country[0]["4/10/21"],chosen_data)).add_to(m)
folium_static(m)
