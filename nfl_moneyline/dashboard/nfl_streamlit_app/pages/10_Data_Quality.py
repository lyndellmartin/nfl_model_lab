import streamlit as st
from lib.data_io import load_csv

st.title("🧪 Data Quality & Pipeline Health")
for name in ["current_week.csv","current_week_features.csv","today_injuries.csv","today_injury_flags.csv","bet_history.csv","line_history.csv"]:
    df = load_csv(name)
    ok = not df.empty
    st.write(f"**{name}** — {'✅ loaded' if ok else '❌ missing'}")
    if ok:
        st.caption(f"{len(df)} rows • {len(df.columns)} cols")
