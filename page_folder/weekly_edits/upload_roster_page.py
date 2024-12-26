import numpy as np
import pandas as pd
import streamlit as st
from streamlit import session_state as ss

def trans_data(roster, program):
    for name in roster[program]:
        if name == "":
            continue
        elif name not in list(ss.staff["Camp_name"]):
            st.error(f"{name} is not in the staff directory.")
        else:
            ss.roster[name] = [program, False]

st.title("Upload Set Roster")
st.write("Set the staff roster for the week")


st.write("Please upload roster in the **exact same** format as the one shown below. The order of the columns does not matter, but the names of the columns (case sensitive) do.")
st.write("Make sure to use **camp names** instead of real names.")
st.image("images/roster_example.png")

roster_file = st.file_uploader("Upload Roster as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])

if roster_file is not None and st.button("Submit File"):
    roster = pd.read_excel(roster_file).fillna("")
    ss.roster = {}  # Resest roster
    # Add names to dict
    programs = ["Impact", "Crew", "Cove", "Workcrew", "Kcrew"]
    for prog in programs:
        trans_data(roster, prog)



# One on ones
st.write("**One on ones**")
oneonone = st.multiselect("Select who has a one on one (babies or crew/impact)", ss.staff["Camp_name"])
if st.button("Save One on One"):
    # Reset 1on1
    for name in ss.roster:
        if ss.roster[name][1] == True:
            ss.roster[name][1] = False
    # Assign 1on1
    for name in oneonone:
        # Check if name is in dict
        if name not in ss.roster:
            st.error(f"{name} is not listed in this weeks roster")
            continue
        ss.roster[name][1] = True


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("**Current Impact**")
    for name in ss.roster:
        if ss.roster[name][0]== "Impact":
            if ss.roster[name][1]:
                st.write(name, " (1on1)")
            else: 
                st.write(name)

with col2:
    st.markdown("**Current Crew**")
    for name in ss.roster:
        if ss.roster[name][0]== "Crew":
            if ss.roster[name][1]:
                st.write(name, " (1on1)")
            else: 
                st.write(name)

with col3:
    st.markdown("**Current Cove**")
    for name in ss.roster:
        if ss.roster[name][0]== "Cove":
            if ss.roster[name][1]:
                st.write(name, " (1on1)")
            else: 
                st.write(name)
                
with col4:
    st.markdown("**Current Workcrew**")
    for name in ss.roster:
        if ss.roster[name][0]== "Workcrew":
            if ss.roster[name][1]:
                st.write(name, " (1on1)")
            else: 
                st.write(name)
                
with col5:
    st.markdown("**Current K-Crew**")
    for name in ss.roster:
        if ss.roster[name][0]== "Kcrew":
            if ss.roster[name][1]:
                st.write(name, " (1on1)")
            else: 
                st.write(name)