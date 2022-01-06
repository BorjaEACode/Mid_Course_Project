import streamlit as st
from data.get import get_country_list
from data.get_communities import get_ccaa_list
from data.functions import create_map, create_graph, radar_plot_ccaa
from data.aux_functions import create_dataframe, create_data_graph
from datetime import datetime


st.title("Covid-19 International Dashboard")

chosen_country = st.multiselect("Select country/countries", get_country_list())
chosen_data = st.selectbox("Select data for map", ["Cases","Deaths","Recovered"])
st.header("Data Map")

create_map(chosen_country, chosen_data)

st.header("Data Graph")
starting_date = st.date_input("Choose a starting date", value=datetime(2020,1,22),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))
ending_date = st.date_input("Choose a ending date", value=datetime(2021,4,10),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))
chosen_data2 = st.selectbox("Select data for graph", ["Cases","Deaths","Recovered"])

df_countries = create_data_graph(chosen_country,chosen_data2,starting_date,ending_date)
figura = create_graph(df_countries,chosen_data2)
st.plotly_chart(figura)

st.title("Covid-19 Spanish Dashboard")

st.header("Data Table")
chosen_ccaa = st.multiselect("Select community/communities", [ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
st.dataframe(create_dataframe(chosen_ccaa))

st.header("Data Radar Plot")
radar_plot = radar_plot_ccaa(chosen_ccaa)
st.plotly_chart(radar_plot)
