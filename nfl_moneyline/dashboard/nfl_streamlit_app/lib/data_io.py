from __future__ import annotations
import streamlit as st
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

@st.cache_data(show_spinner=False)
def load_csv(name_or_path: str) -> pd.DataFrame:
    p = Path(name_or_path)
    if not p.exists():
        p = DATA_DIR / name_or_path
    if not p.exists():
        return pd.DataFrame()
    return pd.read_csv(p)

@st.cache_data(show_spinner=False)
def list_data_files() -> list[str]:
    if not DATA_DIR.exists():
        return []
    return sorted([p.name for p in DATA_DIR.glob("*.csv")])

def save_csv(df: pd.DataFrame, name: str) -> None:
    p = DATA_DIR / name
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
