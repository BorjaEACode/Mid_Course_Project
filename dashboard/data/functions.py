from os import name
from streamlit_folium import folium_static
import folium
import streamlit as st
import plotly.io as pio
import plotly.graph_objs as go
from data.get import get_country_coord, get_country_data
from data.get_communities import get_ccaa_full_data

#INTERNATIONAL FUNCTIONS

def create_coord_list(listacountries):
    listacoordcountries = []
    for country in listacountries:
        listacoordcountries.append(get_country_coord(country))
    return listacoordcountries

def create_data_list(listacountries, chosen_data):
    listadatacountries = []
    for country in listacountries:
        listadatacountries.append(get_country_data(country, chosen_data))
    return listadatacountries

def create_graph(listacountries, chosen_data):
    return


def create_map(listacountries,chosen_data):
    m = folium.Map(location=[0,0], zoom_start=2)
    listacoordcountries = create_coord_list(listacountries)
    listadatacountries = create_data_list(listacountries,chosen_data)
    for i in range(len(listacountries)):
        folium.Marker((listacoordcountries[i][0]["Lat"],listacoordcountries[i][0]["Long"]), popup=listacountries[i], tooltip=(listacountries[i],listadatacountries[i][0]["4/10/21"],f"Total {chosen_data}")).add_to(m)
    return folium_static(m)

#NATIONAL FUNCTIONS

def create_data_list_ccaa(listaccaa):
    listavaccinesccaa = []
    for ccaa in listaccaa:
        listavaccinesccaa.append(get_ccaa_full_data(ccaa))
    return listavaccinesccaa

def create_table(listaccaa):
    listadataccaa = create_data_list_ccaa(listaccaa)
    return st.dataframe(listadataccaa)

# pio.renderers.default = 'notebook'
def radar_plot_ccaa(listaccaa):
    listavaccinesccaa = create_data_list_ccaa(listaccaa)
    fig = go.Figure()
    for ccaa in listavaccinesccaa:
        theta = ["Población", "Total Dosis Entregadas","Total Dosis Administradas","Total Pauta Completa"]
        values = []
        for a in theta:
            values.append(ccaa[0][a])
        fig.add_trace(go.Scatterpolar(
                            r=values,
                            theta=theta,
                            fill="toself",
                            name=ccaa[0]["Comunidad autónoma"]
                                ))
          
    return fig   
