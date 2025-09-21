from __future__ import annotations
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import joblib

MODELS_DIR = Path(__file__).resolve().parents[1] / "models"

@st.cache_resource(show_spinner=False)
def load_model(path_or_name: str):
    p = Path(path_or_name)
    if not p.exists():
        p = MODELS_DIR / path_or_name
    if not p.exists():
        return None
    return joblib.load(p)

def score_probability(model, features_df: pd.DataFrame) -> np.ndarray:
    if model is None:
        return np.full(len(features_df), 0.5, dtype=float)
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features_df)
        if proba.ndim == 2 and proba.shape[1] >= 2:
            return proba[:, 1]
        return proba.ravel()
    if hasattr(model, "predict"):
        y = model.predict(features_df)
        y = np.clip(np.array(y, dtype=float), 0, 1)
        return y
    return np.full(len(features_df), 0.5, dtype=float)
