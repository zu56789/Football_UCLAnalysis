import pandas as pd
from pandas import json_normalize
import requests

def get_data(source): #method to get data from a url
    match_data = requests.get(source)
    match_data = match_data.json()
    df = json_normalize(match_data)
    pd.set_option("display.max.columns", None)
    return df


def get_passing_df(team):
    return events_df.loc[(events_df['type.name'] == 'Pass') & (events_df['possession_team.name'] == team)]

def get_shooting_df(team):
    return events_df.loc[(events_df['type.name'] == 'Shot') & (events_df['possession_team.name'] == team)]

events_df = get_data("https://raw.githubusercontent.com/statsbomb/open-data/refs/heads/master/data/events/18237.json")

chels_passes_df = get_passing_df("Chelsea")
bayern_passes_df = get_passing_df("Bayern Munich")

chels_shots_df = get_shooting_df("Chelsea")
bayern_shots_df = get_shooting_df("Bayern Munich")

#print(events_df.head())