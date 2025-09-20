from __future__ import annotations
import plotly.express as px
import pandas as pd

def line_timeseries(df: pd.DataFrame, x: str, y: str, color: str|None=None, title: str|None=None):
    return px.line(df, x=x, y=y, color=color, title=title)
