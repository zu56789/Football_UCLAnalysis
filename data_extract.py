import pandas as pd
from pandas import json_normalize
import requests

def get_data(source): #method to get data from a url
    match_data = requests.get(source)
    match_data = match_data.json()
    df = json_normalize(match_data)
    pd.set_option("display.max.columns", None)
    return df

events_df = get_data("https://raw.githubusercontent.com/statsbomb/open-data/refs/heads/master/data/events/18237.json")

print(events_df.head())