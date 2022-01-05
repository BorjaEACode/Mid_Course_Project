from os import name
from pandas.core.accessor import PandasDelegate
from streamlit_folium import folium_static
import folium
import streamlit as st
import plotly.io as pio
import plotly.graph_objs as go
import pandas as pd
from data.get_communities import get_ccaa_full_data
from data.aux_functions import create_coord_list, create_data_list, create_data_list_ccaa

#INTERNATIONAL FUNCTIONS

def create_graph(listacountries, chosen_data, starting_date, ending_date):
    listadatacountries = create_data_list(listacountries,chosen_data)
    starting_date_ok = change_date(starting_date)
    ending_date_ok = change_date(ending_date)
    return None

def create_map(listacountries,chosen_data):
    m = folium.Map(location=[0,0], zoom_start=2)
    listacoordcountries = create_coord_list(listacountries)
    listadatacountries = create_data_list(listacountries,chosen_data)
    for i in range(len(listacountries)):
        folium.Marker((listacoordcountries[i][0]["Lat"],listacoordcountries[i][0]["Long"]), popup=listacountries[i], tooltip=(listacountries[i],listadatacountries[i][-1][f"{chosen_data}"],f"Total {chosen_data}")).add_to(m)
    return folium_static(m)

#NATIONAL FUNCTIONS

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
