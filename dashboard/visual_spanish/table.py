import pandas as pd
from data.get_communities import get_ccaa_basic_data


def create_table(listaccaa):
    listafulldataccaa = [(get_ccaa_basic_data(ccaa)) for ccaa in listaccaa]
    df_ccaa = pd.DataFrame()
    for i in range(0,len(listafulldataccaa)):
        df_ccaa= df_ccaa.append(pd.DataFrame(listafulldataccaa[i]))
    return df_ccaa
