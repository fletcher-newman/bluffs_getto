import streamlit as st
from streamlit import session_state as ss
import pandas as pd

st.title("Get To Schedule")
st.write('Be sure to click "Save Changes" once you are done making changes.')
st.write("Don't click off of this tab until you are done and have hit save, or else your edits will not be saved!")
# df is getting edited
# old_sced = ss.sched
new_sched = st.data_editor(ss.sched, num_rows='dynamic')

# Save changes 
if st.button('Save Changes'):
    if new_sched.equals(ss['sched']):
        st.error('No new changes were made')
    else:
        ss['sched'] = new_sched
        new_sched.to_excel('permanent_data/get_to_schedule.xlsx', index=False)
        st.success("Schedule changes saved!")


# Schedule upload section 
st.title("Upload new schedule")
st.page_link("page_folder/formats_page.py", label="**Example formatts can be downloaded in the formatts section** (link)")
st.write("Follow the **exact** same formatting as in the image below. All time must me in military time with no ':' characters.")
st.write("Make sure everything is spelled correctly and that there are no extra spaces around the column names")
st.write("To indicate if an activity happens on a certain day, that cell is marked with a 1 for TRUE and a 0 for FALSE (activity does not happen that day)")
st.write("Ex: Sunrise breakfast needs someone there on Monday, but does not need someone on Sunday (seen bellow)")
st.image("images/sched_example.png")
sched_file = st.file_uploader("Upload K-crew schedule as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])

if sched_file is not None and st.button("Submit File"):
    sched_df = pd.read_excel(sched_file).fillna("")
    sched_df[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']] = sched_df[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].astype(bool)
    ss.sched = sched_df
    st.success("File saved successfully")