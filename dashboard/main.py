from folium.map import Tooltip
import streamlit as st
from data.get import get_country_list, get_country_data, get_country_coord

from streamlit_folium import folium_static
import folium

st.title("Covid-19 Dashboard")
st.text("This is a streamlit display for visualizing data about Covid-19")

chosen_country = st.selectbox("Select one country", [country["Country/Region"] for country in get_country_list()])
chosen_data = st.selectbox("Select data type", ["Cases","Deaths","Recovered"])

data_country = get_country_data(chosen_country, chosen_data)
coord_country = get_country_coord(chosen_country)

st.text("")
st.text("Its coordinates are: ")
st.text(data_country)

st.text("")
st.text("Its data is: ")
st.text(coord_country)

st.text("")
st.line_chart(data=data_country)

m = folium.Map(location=[0,0], zoom_start=16)
folium.Marker([0,0], popup=chosen_country, tooltip=chosen_country).add_to(m)
folium_static(m)
