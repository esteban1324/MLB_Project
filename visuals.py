import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def plot_pitching_stats(player):
    fig = px.line(player, x="Season", y=player.columns[3:6], title="Seasons vs ERA, xERA, FIP, xFIP")
    pitcher = player["Name"].values[0]
    
    fig.update_layout(title_text=f"{pitcher}: Seasons vs ERA, xERA, FIP, xFIP")
    fig.update_xaxes(title_text="Season")
    fig.update_yaxes(title_text="Stats")
    
    return fig 

def plot_pitching_stats2(player):
    fig = px.bar(player, x="Season", y=player.columns[7:11])
    pitcher = player["Name"].values[0]
    fig.update_layout(title_text=f"{pitcher}: Seasons vs FB%, GB%, LD%, K%, BB%")
    fig.update_xaxes(title_text="Season")
    fig.update_yaxes(title_text="Stats")


    return fig 

def plot_batting_stats(player):
    fig = make_subplots(rows=1, cols=3)

    fig.add_trace(go.Scatter(x=player["Season"], y=player["HR"], name="HR"), row=1, col=1)
    fig.add_trace(go.Scatter(x=player["Season"], y=player["AVG"], name="AVG"), row=1, col=2)
    fig.add_trace(go.Scatter(x=player["Season"], y=player["OPS"], name="OPS"), row=1, col=3)
    
    # add title and labels
    hitter = player["Name"].values[0]
    fig.update_layout(title_text=f"{hitter}: Seasons vs HR, AVG, OPS")
    fig.update_xaxes(title_text="Season")
    fig.update_yaxes(title_text="Stats")

    fig.show()
    return fig

def plot_batting_stats2(player):
    fig = make_subplots(rows=1, cols=4)

    fig.add_trace(go.Bar(x=player["Season"], y=player["GB%"], name="GB%"), row=1, col=1)
    fig.add_trace(go.Bar(x=player["Season"], y=player["FB%"], name="FB%"), row=1, col=2)
    fig.add_trace(go.Bar(x=player["Season"], y=player["K%"], name="K%"), row=1, col=3)
    fig.add_trace(go.Bar(x=player["Season"], y=player["BB%"], name="BB%"), row=1, col=4)

    hitter = player["Name"].values[0]
    fig.update_layout(title_text=f"{hitter}: Seasons vs GB%, FB%, K%, BB%")
    fig.update_xaxes(title_text="Season")
    fig.update_yaxes(title_text="Stats")

    fig.show()
    return fig

# sabermetrics plotting functions

