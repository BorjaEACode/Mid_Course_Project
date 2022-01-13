import plotly.graph_objs as go
from data.get_communities import get_ccaa_full_data

def create_radar_plot(listaccaa):
    listavaccinesccaa = [(get_ccaa_full_data(ccaa)) for ccaa in listaccaa]
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
