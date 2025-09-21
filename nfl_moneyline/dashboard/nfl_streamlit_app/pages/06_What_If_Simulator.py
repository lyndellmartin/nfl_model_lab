import streamlit as st
from lib.odds_utils import prob_to_moneyline

st.title("🧪 What-If Simulator")
p = st.slider("Model probability (home)", 0.0, 1.0, 0.55, 0.01)
st.metric("Fair Moneyline (home)", f"{prob_to_moneyline(p):+d}")
