import numpy as np
import pandas as pd
import streamlit as st
from streamlit import session_state as ss
from function_def import trans_kcrew

st.title("K-crew Schedule Upload")

kcrew_file = st.file_uploader("Upload K-crew schedule as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])

if kcrew_file is not None and st.button("Submit File"):
    kcrew_df = pd.read_excel(kcrew_file).fillna("")
    ss.kcrew = {}  # Resest kcrew dict
    st.dataframe(kcrew_df)
    # Add names to dict
    trans_kcrew(kcrew_df)
    for name in ss.kcrew:
        ss.roster[name] = ["Kcrew", False]




