from streamlit_folium import folium_static
import folium
import plotly.graph_objs as go
import plotly.express as px
from data.aux_functions import create_coord_list, create_data_list, create_data_list_ccaa

#INTERNATIONAL FUNCTIONS

def create_graph(df_countries,chosen_data):
    if df_countries.empty==True:
        return px.line()
    else:
        figure = px.line (df_countries, x="Date", y=f"{chosen_data}", color="Country/Region")
    return figure

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
