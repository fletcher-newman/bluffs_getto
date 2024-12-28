import streamlit as st
from streamlit import session_state as ss
import pandas as pd
from function_def import find_bstud

st.title("Upload Bible Study List")
st.write("**Highly** suggest downloading a sample format and modifying it to your specifications.")
st.page_link("page_folder/formats_page.py", label="**Example formatts can be downloaded in the formatts section** (link)")
st.write("Follow the **exact** formatting as shown in the image bellow.")
st.write("Columns are formatted as '<Day> <Start-time>'")
st.write("Gender does not matter, as long as the seperate gender Bible studies have the same start time.")
st.image("images/bstud_example.png")

bstud_file = st.file_uploader("Upload Get-to schedule as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])

# Save uploaded file
if bstud_file is not None and st.button("Submit File"):
    bstud_df = pd.read_excel(bstud_file).fillna("")
    ss.bstud = bstud_df
    # Add data to roster dict 
    for name in ss.roster:
        ss.roster[name]["Bstud_day"], ss.roster[name]["Bstud_time"] = find_bstud(name)
    # Save in long term memory 
    bstud_df.to_excel('permanent_data/bstud_list.xlsx', index=False)
    st.success("File saved successfully")
