import plotly.graph_objs as go
from data.get_communities import get_ccaa_full_data

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
