import plotly.express as px


def create_graph(df_countries,chosen_data):
    if df_countries.empty==True:
        return px.line()
    else:
        figure = px.line (df_countries, x="Date", y=f"{chosen_data}", color="Country/Region")
    return figure
