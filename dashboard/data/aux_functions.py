from data.get import get_country_coord, get_country_data, get_country_all_data, get_country_data_date, get_country_data_between_date, get_country_all_data_date
from data.get_communities import get_ccaa_full_data, get_ccaa_basic_data
import pandas as pd

#INTERNATIONAL AUX FUNCTIONS

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

def create_all_data_list(listacountries):
    listadatacountries = []
    for country in listacountries:
        listadatacountries.append(get_country_all_data(country))
    return listadatacountries

def create_data_date_list(listacountries, chosen_data, date):
    listadatadatecountries = []
    for country in listacountries:
        listadatadatecountries.append(get_country_data_date(country,chosen_data,date))
    return listadatadatecountries

def create_all_data_date_list(listacountries, date):
    listadatadatecountries = []
    for country in listacountries:
        listadatadatecountries.append(get_country_all_data_date(country,date))
    return listadatadatecountries

def create_data_graph(listacountries,chosen_data,date1,date2):
    df_countries=pd.DataFrame()
    for country in listacountries:
        datos_dic = get_country_data_between_date(country,chosen_data,date1,date2)
        for i in range(len(datos_dic)):
            datos_dic[i]["Date"] = datos_dic[i]["Date"]["$date"]
        df_countries = df_countries.append(datos_dic)
    return df_countries

#NATIONAL AUX FUNCTIONS

def create_data_list_ccaa(listaccaa):
    if (listaccaa)==None:
        return None
    else:
        listavaccinesccaa = []
        for ccaa in listaccaa:
            listavaccinesccaa.append(get_ccaa_full_data(ccaa))
        return listavaccinesccaa

def create_basic_data_list_ccaa(listaccaa):
    if (listaccaa)==None:
        return None
    else:
        listavaccinesccaa = []
        for ccaa in listaccaa:
            listavaccinesccaa.append(get_ccaa_basic_data(ccaa))
        return listavaccinesccaa
