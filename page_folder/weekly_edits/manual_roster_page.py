import numpy as np
import pandas as pd
import streamlit as st
from streamlit import session_state as ss

st.title("Manual Set Roster")
st.write("Set the staff roster for the week")

#Impact
impact_temp = st.multiselect("**Impact:**", ss["staff"]["Camp_name"])
for name in impact_temp:
    st.write(name)

if st.button("Save Impact"):
    # Delete Current Impact
    ss.roster = {campName: valList for campName, valList in ss.roster.items() if valList[0] != "Impact"}
    # Add new impact
    for name in impact_temp:
        if name in ss.roster:
            ss.roster[name][0] = "Impact"
        else:
            ss.roster[name] = ["Impact", False]



#crew
crew_temp = st.multiselect("**Crew:**", ss["staff"]["Camp_name"])
for name in crew_temp:
    st.write(name)

if st.button("Save Crew"):
    # Delete Current Crew
    ss.roster = {campName: valList for campName, valList in ss.roster.items() if valList[0] != "Crew"}
    # Add new impact
    for name in crew_temp:
        if name in ss.roster:
            ss.roster[name][0] = "Crew"
        else:
            ss.roster[name] = ["Crew", False]



#cove
cove_temp = st.multiselect("**Cove:**", ss["staff"]["Camp_name"])
for name in cove_temp:
    st.write(name)

if st.button("Save Cove"):
    # Delete Current Cove
    ss.roster = {campName: valList for campName, valList in ss.roster.items() if valList[0] != "Cove"}
    # Add new impact
    for name in cove_temp:
        if name in ss.roster:
            ss.roster[name][0] = "Cove"
        else:
            ss.roster[name] = ["Cove", False]



#workcrew
wc_temp = st.multiselect("**Work Crew:**", ss["staff"]["Camp_name"])
for name in wc_temp:
    st.write(name)

if st.button("Save Work Crew"):
    # Delete Current Workcrew
    ss.roster = {campName: valList for campName, valList in ss.roster.items() if valList[0] != "Workcrew"}
    # Add new workcrew
    for name in wc_temp:
        ss.roster[name] = ["Workcrew", False]



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
                
