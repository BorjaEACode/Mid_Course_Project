from streamlit_folium import folium_static
import folium
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from data.aux_functions import create_coord_list, create_data_date_list, create_data_list, create_data_list_ccaa, get_ccaa_full_data, create_basic_data_list_ccaa

#INTERNATIONAL FUNCTIONS

def create_dataframe_countries(listacountries,chosen_data):
    listadfcountries = create_data_date_list(listacountries,chosen_data, "2021-04-10")
    df_countries = pd.DataFrame()
    for i in range(0,len(listadfcountries)):
        df_countries= df_countries.append(pd.DataFrame(listadfcountries[i]))
        df_countries.pop("Date")
    return df_countries

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

def create_dataframe(listaccaa):
    listafulldataccaa = create_basic_data_list_ccaa(listaccaa)
    df = pd.DataFrame()
    for i in range(0,len(listafulldataccaa)):
        df= df.append(pd.DataFrame(listafulldataccaa[i]))
    return df

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

def create_pie_chart(chosen_pie_ccaa):
    if chosen_pie_ccaa==None:
        return go.Pie()
    elif chosen_pie_ccaa:
        datos_chart = get_ccaa_full_data(chosen_pie_ccaa)
        labels = ["Pfizer Entregadas","Moderna Entregadas","AstraZeneca Entregadas","Janssen Entregadas"]
        values = []
        for dato in datos_chart:
            for label in labels:
                values.append(dato[f"{label}"])
        pie_chart = go.Figure(data=[go.Pie(labels=labels,values=values, title=chosen_pie_ccaa,hole=.3)])
        return pie_chart

