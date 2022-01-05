from data.get import get_country_coord, get_country_data, get_country_data_date, get_country_data_between_date
from data.get_communities import get_ccaa_full_data
from datetime import datetime, timedelta
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

def create_data_date_list(listacountries, chosen_data, date):
    listadatadatecountries = []
    for country in listacountries:
        listadatadatecountries.append(get_country_data_date(country,chosen_data,date))
    return listadatadatecountries

def create_data_graph(listacountries,chosen_data,date1,date2):
    df_countries=pd.DataFrame()
    for country in listacountries:
        df_countries = df_countries.append(get_country_data_between_date(country,chosen_data,date1,date2))
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

def create_dataframe(listaccaa):
    listafulldataccaa = create_data_list_ccaa(listaccaa)
    df = pd.DataFrame()
    for i in range(0,len(listafulldataccaa)):
        df= df.append(pd.DataFrame(listafulldataccaa[i]))
    return df
