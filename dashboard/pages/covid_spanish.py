import streamlit as st
from data.get_communities import get_ccaa_list
from data.visualizers import radar_plot_ccaa, create_dataframe, create_pie_chart


def covid_spanish():
    st.header("Spanish Dashboard")

    chosen_ccaa = st.multiselect("Select community/communities", [ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
    st.header("Total Data Table")
    df_ccaa = (create_dataframe(chosen_ccaa))
    st.dataframe(df_ccaa)

    st.header("Doses Data Radar Plot")
    radar_plot = radar_plot_ccaa(chosen_ccaa)
    st.plotly_chart(radar_plot)

    st.header("Vaccine Delivered Pie Chart")
    chosen_pie_ccaa = st.selectbox("Select community", [ccaa["Comunidad autónoma"] for ccaa in get_ccaa_list()])
    pie_chart = create_pie_chart(chosen_pie_ccaa)
    st.plotly_chart(pie_chart)
