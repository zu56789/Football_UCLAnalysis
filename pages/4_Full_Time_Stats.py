import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from data_extract import chels_passes_df, bayern_passes_df, chels_shots_df, bayern_shots_df
from metric_analysis import get_passing_accuracy, get_xg, get_shot_accuracy

chels_passing_accuracy = get_passing_accuracy(chels_passes_df)[0]
chels_total_passes = get_passing_accuracy(chels_passes_df)[1]
chels_completed_passes = get_passing_accuracy(chels_passes_df)[2]

chels_xg = get_xg(chels_shots_df)
chels_shot_accuracy = get_shot_accuracy(chels_shots_df)[0]
chels_num_shots = get_shot_accuracy(chels_shots_df)[1]
chels_shots_on_target = get_shot_accuracy(chels_shots_df)[2]
chels_shots_off_target = get_shot_accuracy(chels_shots_df)[3]

bayern_passing_accuracy = get_passing_accuracy(bayern_passes_df)[0]
bayern_total_passes = get_passing_accuracy(bayern_passes_df)[1]
bayern_completed_passes = get_passing_accuracy(bayern_passes_df)[2]

bayern_xg = get_xg(bayern_shots_df)
bayern_shot_accuracy = get_shot_accuracy(bayern_shots_df)[0]
bayern_num_shots = get_shot_accuracy(bayern_shots_df)[1]
bayern_shots_on_target = get_shot_accuracy(bayern_shots_df)[2]
bayern_shots_off_target = get_shot_accuracy(bayern_shots_df)[3]