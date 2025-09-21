import streamlit as st
from lib.data_io import load_csv

st.title("🔎 Feature Explorer")
features = load_csv("current_week_features.csv")
if features.empty:
    st.warning("`current_week_features.csv` not found.")
else:
    num_cols = [c for c in features.columns if str(features[c].dtype) != "object"]
    col = st.selectbox("Pick a feature", num_cols)
    st.line_chart(features[col])
    st.dataframe(features[[c for c in ["game_id","home_team","away_team", col] if c in features.columns]])
