import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_pitching_stats(player):
    fig = px.line(player, x="Season", y=player.columns[3:6], title="Seasons vs ERA, xERA, FIP, xFIP")
    return fig 

def plot_pitching_stats2(player):
    fig = px.bar(player, x="Season", y=player.columns[7:11])
    return fig 

def plot_batting_stats(player):
    fig = px.line(player, x="Season", y=player.columns[1:7], title="Seasons vs HR, AVG, OPS, ISO, wOBA, wRC+, WAR, BABIP, GB%, FB%, K%, BB%, Barrel%, HardHit%")
    

def plot_batting_stats2(player):
    fig = px.bar(player, x="Season", y=player.columns[8:13])
    

