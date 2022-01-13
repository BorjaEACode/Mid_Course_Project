from data.get import get_country_data_between_date
import pandas as pd


def create_data_graph(listacountries,chosen_data,date1,date2):
    df_countries=pd.DataFrame()
    for country in listacountries:
        datos_dic = get_country_data_between_date(country,chosen_data,date1,date2)
        for i in range(len(datos_dic)):
            datos_dic[i]["Date"] = datos_dic[i]["Date"]["$date"]
        df_countries = df_countries.append(datos_dic)
    return df_countries
