import pandas as pd
from data.get import get_country_all_data_date


def dataframe_countries(listacountries):
    listadfcountries = [(get_country_all_data_date(country, "2021-04-10")) for country in listacountries]
    df_countries = pd.DataFrame()
    for i in range(0,len(listadfcountries)):
        df_countries= df_countries.append(pd.DataFrame(listadfcountries[i]))
        df_countries.pop("Date")
    return df_countries
