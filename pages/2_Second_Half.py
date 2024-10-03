import streamlit as st
from data_extract import chels_passes_df, bayern_passes_df, chels_shots_df, bayern_shots_df
from draw_pitches import passing_pitch, shooting_pitch
from metric_analysis import get_passing_accuracy, get_xg

st.set_page_config(page_title="Second Half")

st.title("Second Half Data")

chels_tab, bayern_tab = st.tabs(["Chelsea", "Bayern Munich"])

with chels_tab:
    st.write("Passing map")
    st.pyplot(passing_pitch(chels_passes_df,2))
    expander = st.expander("Passing stats")
    expander.write("Passing accuracy: " + str(get_passing_accuracy(chels_passes_df, 2)[0]) + "%")
    st.write("Shooting map")
    st.pyplot(shooting_pitch(chels_shots_df,2))
    expander = st.expander("Shooting stats")
    expander.write("Expected Goals: " + str(get_xg(chels_shots_df, 2)))

with bayern_tab:
    st.write("Passing map")
    st.pyplot(passing_pitch(bayern_passes_df,2))
    expander = st.expander("Passing stats")
    expander.write("Passing accuracy: " + str(get_passing_accuracy(bayern_passes_df, 2)[0]) + "%")
    st.write("Shooting map")
    st.pyplot(shooting_pitch(bayern_shots_df,2))
    expander = st.expander("Shooting stats")
    expander.write("Expected Goals: " + str(get_xg(bayern_shots_df, 2)))