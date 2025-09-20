import streamlit as st
st.title("💰 Bankroll & Sizing")
bankroll = st.number_input("Bankroll ($)", min_value=0.0, value=1000.0, step=50.0)
max_stake_pct = st.slider("Max stake per bet (%)", 0.0, 10.0, 2.0, 0.25)
st.caption("Use this with Kelly outputs in Value Finder to cap stakes.")
