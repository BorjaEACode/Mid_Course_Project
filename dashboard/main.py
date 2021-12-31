import streamlit as st
from data.get import get_list_country, get_data_country

st.title("Covid-19 Dashboard")
st.text("This is a streamlit display for visualizing data about Covid-19")

chosen_data = st.selectbox("Select data type", ["Cases","Deaths","Recovered"])
chosen_country = st.selectbox("Select one country", [country["Country/Region"] for country in get_list_country()])

data_country = get_data_country(chosen_country, chosen_data)

st.text(data_country)
