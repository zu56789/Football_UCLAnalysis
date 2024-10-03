import streamlit as st
from data_extract import chels_passes_df, bayern_passes_df, chels_shots_df, bayern_shots_df
from draw_pitches import passing_pitch, shooting_pitch
from metric_analysis import get_passing_accuracy, get_xg, get_shot_accuracy

st.set_page_config(page_title="Extra Time 2")

st.title("Extra time 2 data")

chels_tab, bayern_tab = st.tabs(["Chelsea", "Bayern Munich"])

with chels_tab:
    st.write("Passing map")
    st.pyplot(passing_pitch(chels_passes_df,4))
    expander = st.expander("Passing stats")
    expander.markdown("""
    - 🔵 **Blue**: Accurate pass
    - 🔴 **Red**: Inaccurate pass
    """)
    expander.write("Passing accuracy: " + str(get_passing_accuracy(chels_passes_df, 4)[0]) + "%")
    expander.write("Passes attempted: " + str(get_passing_accuracy(chels_passes_df, 4)[1]))
    expander.write("Passes completed: " + str(get_passing_accuracy(chels_passes_df, 4)[2]))
    st.write("Shooting map")
    st.pyplot(shooting_pitch(chels_shots_df,4))
    expander = st.expander("Shooting stats")
    expander.markdown("""
    - 🔵 **Blue**: Goal
    - 🔴 **Red**: No Goal
    - **Bigger circle**: Higher xg shot
    """)
    expander.write("Expected Goals: " + str(get_xg(chels_shots_df, 4)))
    expander.write("Shot accuracy: " + str(get_shot_accuracy(chels_shots_df, 4)[0]) + "%")
    expander.write("Shot attempts: " + str(get_shot_accuracy(chels_shots_df, 4)[1]))
    expander.write("Shots on target: " + str(get_shot_accuracy(chels_shots_df, 4)[2]))
    expander.write("Shots off target: " + str(get_shot_accuracy(chels_shots_df, 4)[3]))

with bayern_tab:
    st.write("Passing map")
    st.pyplot(passing_pitch(bayern_passes_df,4))
    expander = st.expander("Passing stats")
    expander.markdown("""
    - 🔵 **Blue**: Accurate pass
    - 🔴 **Red**: Inaccurate pass
    """)
    expander.write("Passing accuracy: " + str(get_passing_accuracy(bayern_passes_df, 4)[0]) + "%")
    expander.write("Passes attempted: " + str(get_passing_accuracy(bayern_passes_df, 4)[1]))
    expander.write("Passes completed: " + str(get_passing_accuracy(bayern_passes_df, 4)[2]))
    st.write("Shooting map")
    st.pyplot(shooting_pitch(bayern_shots_df,4))
    expander = st.expander("Shooting stats")
    expander.markdown("""
    - 🔵 **Blue**: Goal
    - 🔴 **Red**: No Goal
    - **Bigger circle**: Higher xg shot
    """)
    expander.write("Expected Goals: " + str(get_xg(bayern_shots_df, 4)))
    expander.write("Shot accuracy: " + str(get_shot_accuracy(bayern_shots_df, 4)[0]) + "%")
    expander.write("Shot attempts: " + str(get_shot_accuracy(bayern_shots_df, 4)[1]))
    expander.write("Shots on target: " + str(get_shot_accuracy(bayern_shots_df, 4)[2]))
    expander.write("Shots off target: " + str(get_shot_accuracy(bayern_shots_df, 4)[3]))