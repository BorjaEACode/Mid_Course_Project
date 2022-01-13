import streamlit as st
from data.get import get_country_list
from datetime import datetime
from visual_international.dataframe import dataframe_countries
from visual_international.map import map_creator
from visual_international.graph import create_graph
from utils.data_graph import create_data_graph


def covid_international():
    st.header("International Dashboard")

    chosen_country = st.multiselect("Select country/countries", get_country_list())
    
    st.header("Total Data Table")
    st.dataframe(dataframe_countries(chosen_country))

    st.header("% Deaths Data Map")
    map_creator(chosen_country)

    st.header("Interval Data Graph")
    chosen_data = st.selectbox("Select data for graph", ["Cases","Deaths","Recovered"])
    starting_date = st.date_input("Choose a starting date", value=datetime(2020,1,22),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))
    ending_date = st.date_input("Choose a ending date", value=datetime(2021,4,10),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))

    st.plotly_chart(create_graph(create_data_graph(chosen_country,chosen_data,starting_date,ending_date),chosen_data))
