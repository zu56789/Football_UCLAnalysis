import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import numpy as np

def passing_pitch(df, half):
    
    fig, ax = plt.subplots(figsize=(27,15))
    pitch = Pitch(pitch_type='statsbomb', pitch_color='black', goal_type='box')

    for x in range(len(df['id'])):
        if df['period'].iloc[x] == half:
            if any([df['pass.outcome.name'].iloc[x] == "Incomplete",
                    df['pass.outcome.name'].iloc[x] == "Unknown",
                    df['pass.outcome.name'].iloc[x] == 'Injury Clearance',
                    df['pass.outcome.name'].iloc[x] == 'Out',
                    df['pass.outcome.name'].iloc[x] == 'Lost Out']):
                
                plt.plot((df['location'].iloc[x][0],df['pass.end_location'].iloc[x][0]),\
                        (df['location'].iloc[x][1],df['pass.end_location'].iloc[x][1]),color='red')
                plt.scatter(df['location'].iloc[x][0],df['location'].iloc[x][1], color='red', s=100)
            else:

                plt.plot((df['location'].iloc[x][0],df['pass.end_location'].iloc[x][0]),\
                        (df['location'].iloc[x][1],df['pass.end_location'].iloc[x][1]),color='blue')
                plt.scatter(df['location'].iloc[x][0],df['location'].iloc[x][1],color='blue', s=100)

    pitch.draw(ax=ax) 

    return fig
    
def shooting_pitch(df,half): 

    fig, ax = plt.subplots(figsize=(18,12))
    pitch = Pitch(pitch_type='statsbomb', pitch_color='black', goal_type='box')

    for x in range(len(df['id'])):
        if df['period'].iloc[x] == half:
            size = np.sqrt(df['shot.statsbomb_xg'].iloc[x])*250 #bigger circle means more xg
            if df['shot.outcome.name'].iloc[x] == 'Goal':       
                plt.scatter(df['location'].iloc[x][0],df['location'].iloc[x][1], color='blue', s=size)
            else:
                plt.scatter(df['location'].iloc[x][0],df['location'].iloc[x][1],color='red', s=size)

    pitch.draw(ax=ax)
    return fig