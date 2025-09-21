import streamlit as st
import pandas as pd
from lib.data_io import load_csv
from lib.odds_utils import moneyline_to_prob

st.title("🗓️ Slate & Odds")
df = load_csv("current_week.csv")
if df.empty:
    st.warning("`data/current_week.csv` not found.")
else:
    if all(c in df.columns for c in ["home_moneyline","away_moneyline"]):
        df["p_market_home"] = df["home_moneyline"].apply(moneyline_to_prob)
        df["p_market_away"] = df["away_moneyline"].apply(moneyline_to_prob)
    cols = st.multiselect("Columns", options=list(df.columns), default=[c for c in ["season","week","date","home_team","away_team","home_moneyline","away_moneyline","p_market_home","p_market_away"] if c in df.columns])
    st.dataframe(df[cols], use_container_width=True)
