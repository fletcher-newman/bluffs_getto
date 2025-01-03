import numpy as np
import pandas as pd
import streamlit as st
from streamlit import session_state as ss
from function_def import trans_kcrew, find_bstud

st.title("K-crew Schedule Upload")

kcrew_file = st.file_uploader("Upload K-crew schedule as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])

if kcrew_file is not None and st.button("Submit File"):
    kcrew_df = pd.read_excel(kcrew_file).fillna("")
    ss.kcrew = {}  # Resest kcrew dict
    st.dataframe(kcrew_df)
    # Add names to kcrew dict
    trans_kcrew(kcrew_df)
    # Add to dict and find bstud time
    for name in ss.kcrew:
        day, time = find_bstud(name)
        ss.roster[name] = {"Role": "Kcrew", "OneOnOne": False, "Bstud_day": day, "Bstud_time": time}
    # Save in long term memory 
    kcrew_df.to_excel('permanent_data/kcrew_schedule.xlsx', index=False)
    st.success("File Uploaded Successfuly")




