import streamlit as st
from lib.data_io import list_data_files

st.set_page_config(page_title="NFL Betting Dashboard", layout="wide")
st.title("🏈 NFL Betting Dashboard")
st.markdown("Use the sidebar to navigate pages.")

st.subheader("Files detected in ./data")
files = list_data_files()
st.write(files if files else "No CSVs yet. Add `current_week.csv` / `current_week_features.csv`.")
