import streamlit as st
from data.get import get_country_list
from data.visualizers import create_map, create_graph, create_dataframe_countries
from data.aux_functions import create_data_graph
from datetime import datetime


def covid_international():
    st.header("International Dashboard")

    chosen_country = st.multiselect("Select country/countries", get_country_list())
    chosen_data = st.selectbox("Select data for map", ["Cases","Deaths","Recovered"])
    
    st.header("Total Data Table")
    df_countries = (create_dataframe_countries(chosen_country,chosen_data))
    st.dataframe(df_countries)

    st.header("Total Data Map")
    create_map(chosen_country, chosen_data)

    st.header("Interval Data Graph")
    starting_date = st.date_input("Choose a starting date", value=datetime(2020,1,22),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))
    ending_date = st.date_input("Choose a ending date", value=datetime(2021,4,10),min_value=datetime(2020,1,22), max_value=datetime(2021,4,10))

    df_countries = create_data_graph(chosen_country,chosen_data,starting_date,ending_date)
    figura = create_graph(df_countries,chosen_data)
    st.plotly_chart(figura)
