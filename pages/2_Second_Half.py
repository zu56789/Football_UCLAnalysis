import streamlit as st
from data_extract import chels_passes_df, bayern_passes_df, chels_shots_df, bayern_shots_df
from draw_pitches import passing_pitch, shooting_pitch

st.set_page_config(page_title="Second Half")

st.title("Second Half Data")

chels_tab, bayern_tab = st.tabs(["Chelsea", "Bayern Munich"])

with chels_tab:
    st.write("Passing map")
    st.pyplot(passing_pitch(chels_passes_df,2))
    st.write("Shooting map")
    st.pyplot(shooting_pitch(chels_shots_df,2))

with bayern_tab:
    st.write("Passing map")
    st.pyplot(passing_pitch(bayern_passes_df,2))
    st.write("Shooting map")
    st.pyplot(shooting_pitch(bayern_shots_df,2))