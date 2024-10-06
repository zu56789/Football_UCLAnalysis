import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from data_extract import chels_passes_df, bayern_passes_df, chels_shots_df, bayern_shots_df
from metric_analysis import get_passing_accuracy, get_xg, get_shot_accuracy

chels_shooting = {
    "Expected Goals": get_xg(chels_shots_df),
    "Shooting Accuracy (%)": get_shot_accuracy(chels_shots_df)[0],
    "Total Shots": get_shot_accuracy(chels_shots_df)[1],
    "Shots on Target": get_shot_accuracy(chels_shots_df)[2],
    "Shots off Target": get_shot_accuracy(chels_shots_df)[3]
}

chels_passing = {
    "Passing Accuracy (%)": get_passing_accuracy(chels_passes_df)[0],
    "Total Pass Attempts": get_passing_accuracy(chels_passes_df)[1],
    "Completed Passes": get_passing_accuracy(chels_passes_df)[2]
}

bayern_shooting = {
    "Expected Goals": get_xg(bayern_shots_df),
    "Shooting Accuracy (%)": get_shot_accuracy(bayern_shots_df)[0],
    "Total Shots": get_shot_accuracy(bayern_shots_df)[1],
    "Shots on Target": get_shot_accuracy(bayern_shots_df)[2],
    "Shots off Target": get_shot_accuracy(bayern_shots_df)[3]
}

bayern_passing = {
    "Passing Accuracy (%)": get_passing_accuracy(bayern_passes_df)[0],
    "Total Pass Attempts": get_passing_accuracy(bayern_passes_df)[1],
    "Completed Passes": get_passing_accuracy(bayern_passes_df)[2]
}

def draw_bar_charts(chels_stats, bayern_stats, labels, title):
    chels_values = list(chels_stats.values())
    bayern_values = list(bayern_stats.values())

    bar_width = 0.3

    fig, ax = plt.subplots(figsize=(12,7))

    bars_chels = ax.barh(np.arange(len(labels)), chels_values, bar_width, label = "Chelsea", color= "blue")

    bars_bayern = ax.barh(np.arange(len(labels)) + bar_width, bayern_values, bar_width, label = "Bayern", color= "red")

    ax.set_xlabel('Values')
    ax.set_title(title)
    ax.set_yticks(np.arange(len(labels)) + bar_width / 2)
    ax.set_yticklabels(labels)
    ax.legend()

    for bar in bars_chels:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, str(bar.get_width()), va='center')
    for bar in bars_bayern:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, str(bar.get_width()), va='center')

    return fig

st.title("Full time stats")

passing_tab, shooting_tab = st.tabs(["Passing stats", "Shooting stats"])

with passing_tab:
    st.header("Passing stats")
    passing_labels = list(chels_passing.keys())
    passing_chart = draw_bar_charts(chels_passing,bayern_passing,passing_labels, "Passing Data Comparison")
    st.pyplot(passing_chart)

with shooting_tab:
    st.header("Shooting stats")
    shooting_labels = list(chels_shooting.keys())
    shooting_chart = draw_bar_charts(chels_shooting,bayern_shooting,shooting_labels, "Shooting Data Comparison")
    st.pyplot(shooting_chart)