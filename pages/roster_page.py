import numpy as np
import pandas as pd
import streamlit as st
from streamlit import session_state as ss

st.title("Set Roster")
st.write("Set the staff roster for the week")

left, right = st.columns(2)
manual = left.button("Manual Entry", use_container_width=True)
auto = right.button("Upload Entry", use_container_width=True)

if manual:
    #Impact
    impact_temp = st.multiselect("**Impact:**", ss["staff"]["Camp_name"])
    for name in impact_temp:
        st.write(name)

    if st.button("Save Impact"):
        ss.impact = pd.DataFrame(impact_temp, columns=["Camp_name"])

    #crew
    crew_temp = st.multiselect("**Crew:**", ss["staff"]["Camp_name"])
    for name in crew_temp:
        st.write(name)

    if st.button("Save Crew"):
        ss.crew = pd.DataFrame(crew_temp, columns=["Camp_name"])

    #cove
    cove_temp = st.multiselect("**Cove:**", ss["staff"]["Camp_name"])
    for name in cove_temp:
        st.write(name)

    if st.button("Save Cove"):
        ss.cove = pd.DataFrame(cove_temp, columns=["Camp_name"])

    #workcrew
    wc_temp = st.multiselect("**Work Crew:**", ss["staff"]["Camp_name"])
    for name in wc_temp:
        st.write(name)

    if st.button("Save Work Crew"):
        ss.workcrew = pd.DataFrame(wc_temp, columns=["Camp_name"])

    #kcrew
    kcrew_temp = st.multiselect("**K-Crew:**", ss["staff"]["Camp_name"])
    for name in kcrew_temp:
        st.write(name)

    if st.button("Save K-Crew"):
        ss.kcrew = pd.DataFrame(kcrew_temp, columns=["Camp_name"])

# Auto upload
else: 
    st.write("Please upload roster in the **exact same** format as the one shown below. The order of the columns does not matter, but the names of the columns (case sensitive) do.")
    st.write("Make sure to use **camp names** instead of real names.")
    st.image("roster_example.png")
    roster_file = st.file_uploader("Upload Roster as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])
    if roster_file is not None and st.button("Submit File"):
        roster = pd.read_excel(roster_file)
        ss.impact = roster["Impact"]
        ss.crew = roster["Crew"]
        ss.cove = roster["Cove"]
        ss.workcrew = roster["Workcrew"]
        ss.kcrew = roster["Kcrew"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("**Current Impact**")
    st.dataframe(ss.impact, hide_index=True)
with col2:
    st.markdown("**Current Crew**")
    st.dataframe(ss.crew, hide_index=True)
with col3:
    st.markdown("**Current Cove**")
    st.dataframe(ss.cove, hide_index=True)
with col4:
    st.markdown("**Current Workcrew**")
    st.dataframe(ss.workcrew, hide_index=True)
with col5:
    st.markdown("**Current K-Crew**")
    st.dataframe(ss.kcrew, hide_index=True) 