import streamlit as st
from lib.data_io import load_csv

st.title("🩹 Injuries & Availability")
inj = load_csv("today_injuries.csv")
flags = load_csv("today_injury_flags.csv")
tab1, tab2 = st.tabs(["Player-level", "Team aggregates"])
with tab1:
    st.dataframe(inj if not inj.empty else "No injury file.")
with tab2:
    st.dataframe(flags if not flags.empty else "No flags file.")
