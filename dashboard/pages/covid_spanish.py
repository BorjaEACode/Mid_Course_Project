import streamlit as st
from data.get_communities import get_ccaa_list
from visual_spanish.radar_plot import create_radar_plot
from visual_spanish.table import create_table
from visual_spanish.pie_chart import create_pie_chart


def covid_spanish():
    
    st.header("Spanish Dashboard")
    

    chosen_ccaa = st.multiselect("Select community/communities", [ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
    st.header("Total Data Table")
    st.dataframe(create_table(chosen_ccaa))
    st.header("Doses Data Radar Plot")
    st.plotly_chart(create_radar_plot(chosen_ccaa))

    st.header("Vaccine Delivered Pie Chart")
    chosen_pie_ccaa_1 = st.selectbox("Select community 1", ["None"]+[ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
    chosen_pie_ccaa_2 = st.selectbox("Select community 2", ["None"]+[ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
    col1,col2 = st.columns(2)
    col1.plotly_chart(create_pie_chart(chosen_pie_ccaa_1))
    col2.plotly_chart(create_pie_chart(chosen_pie_ccaa_2))
