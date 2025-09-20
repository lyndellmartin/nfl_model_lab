import streamlit as st
import pandas as pd
from lib.data_io import load_csv, save_csv

st.title("📒 Bet Tracker & Performance")
bets = load_csv("bet_history.csv")
with st.form("new_bet"):
    date = st.date_input("Date")
    game = st.text_input("Game (e.g., BUF @ KC)")
    side = st.selectbox("Side", ["Home","Away"])
    price = st.number_input("Price (ML, e.g., -120 or +150)", step=1.0)
    stake = st.number_input("Stake ($)", min_value=0.0, value=10.0, step=1.0)
    result = st.selectbox("Result", ["Pending","Win","Loss","Push"])
    submitted = st.form_submit_button("Add bet")
    if submitted:
        row = {"date":str(date),"game":game,"side":side,"price":price,"stake":stake,"result":result}
        bets = pd.concat([bets, pd.DataFrame([row])], ignore_index=True) if not bets.empty else pd.DataFrame([row])
        save_csv(bets, "bet_history.csv")
        st.success("Bet added.")
st.dataframe(bets if not bets.empty else "No bets yet.")
