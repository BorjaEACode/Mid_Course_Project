from data.get import get_country_coord, get_country_all_data
from streamlit_folium import folium_static
import folium


def map_creator(listacountries):
    m = folium.Map(location=[0,0], zoom_start=2)
    listacoordcountries = [(get_country_coord(country)) for country in listacountries]
    listadatacountries = [(get_country_all_data(country)) for country in listacountries]
    for i in range(len(listacountries)):
        folium.Marker((listacoordcountries[i][0]["Lat"],listacoordcountries[i][0]["Long"]), popup=listacountries[i], tooltip=(((listacountries[i],"{:.4f}".format(listadatacountries[i][-1]["Deaths"]/listadatacountries[i][-1]["Cases"]*100),"%")))).add_to(m)
    return folium_static(m)
