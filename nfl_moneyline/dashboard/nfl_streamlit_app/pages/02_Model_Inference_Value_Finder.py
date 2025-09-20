import streamlit as st
import pandas as pd
import numpy as np
from lib.data_io import load_csv
from lib.model_io import load_model, score_probability
from lib.odds_utils import moneyline_to_prob, fair_moneyline_from_prob, kelly_fraction

st.title("🎯 Model Inference — Value Finder")

model_name = st.text_input("Model filename (in models/)", "model.joblib")
kelly_frac = st.slider("Kelly fraction", 0.0, 1.0, 0.5, 0.05)
min_edge_pct = st.slider("Min edge (%)", 0.0, 10.0, 2.0, 0.25)

features = load_csv("current_week_features.csv")
slate = load_csv("current_week.csv")

if features.empty or slate.empty:
    st.warning("Need both `current_week_features.csv` and `current_week.csv`.")
    st.stop()

for col in ["home_moneyline","away_moneyline"]:
    if col not in slate.columns:
        slate[col] = np.nan

df = slate.merge(features, on="game_id", how="left", suffixes=("","_feat"))
drop_like = {"game_id","season","week","date","home_team","away_team","home_moneyline","away_moneyline","Winner"}
num_cols = [c for c in features.columns if c not in drop_like and features[c].dtype != "O"]
X = df[num_cols].copy()

model = load_model(model_name)
p_home = score_probability(model, X)
df["p_model_home"] = p_home
df["p_model_away"] = 1 - p_home

df["p_market_home"] = df["home_moneyline"].apply(moneyline_to_prob)
df["p_market_away"] = df["away_moneyline"].apply(moneyline_to_prob)

df["edge_home"] = (df["p_model_home"] - df["p_market_home"]) * 100
df["edge_away"] = (df["p_model_away"] - df["p_market_away"]) * 100

df["fair_ml_home"] = df["p_model_home"].apply(fair_moneyline_from_prob)
df["fair_ml_away"] = df["p_model_away"].apply(fair_moneyline_from_prob)

df["stake_home_pct"] = [kelly_frac*100*max(0.0, ((p*(1+(100/(-ml)) if ml<0 else 1+(ml/100)) - 1) / ((1+(100/(-ml)) if ml<0 else 1+(ml/100)) - 1))) if pd.notna(ml) else 0 for p, ml in zip(df["p_model_home"], df["home_moneyline"])]

show = df[["season","week","home_team","away_team","home_moneyline","away_moneyline","p_market_home","p_model_home","edge_home","fair_ml_home","p_market_away","p_model_away","edge_away","fair_ml_away"]]
st.dataframe(show[(show["edge_home"].abs() >= min_edge_pct) | (show["edge_away"].abs() >= min_edge_pct)], use_container_width=True)
