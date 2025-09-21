import streamlit as st
from lib.data_io import load_csv
from lib.visuals import line_timeseries

st.title("📈 Line Movement & Market Heatmap")
hist = load_csv("line_history.csv")
if hist.empty:
    st.info("No `line_history.csv` detected.")
else:
    game_ids = sorted(hist["game_id"].unique())
    game = st.selectbox("Pick a game", game_ids)
    h = hist[hist["game_id"]==game].sort_values("timestamp")
    st.plotly_chart(line_timeseries(h, x="timestamp", y="moneyline", color="book", title="Moneyline over time"), use_container_width=True)
