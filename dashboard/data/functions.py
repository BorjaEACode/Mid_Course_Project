from streamlit_folium import folium_static
import folium
from data.get import get_country_coord, get_country_data

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


def create_map(listacountries,chosen_data):
    m = folium.Map(location=[0,0], zoom_start=2)
    listacoordcountries = create_coord_list(listacountries)
    listadatacountries = create_data_list(listacountries,chosen_data)
    for i in range(len(listacountries)):
        folium.Marker((listacoordcountries[i][0]["Lat"],listacoordcountries[i][0]["Long"]), popup=listacountries[i], tooltip=(listacountries[i],listadatacountries[i][0]["4/10/21"],chosen_data)).add_to(m)
    return folium_static(m)
