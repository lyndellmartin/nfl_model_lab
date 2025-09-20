import streamlit as st
from pathlib import Path

st.title("⚙️ Settings & Model Registry")
uploaded = st.file_uploader("Upload a .joblib model", type=["joblib","pkl"])
if uploaded:
    path = Path("models") / uploaded.name
    with open(path, "wb") as f:
        f.write(uploaded.getvalue())
    st.success(f"Saved to {path}")
