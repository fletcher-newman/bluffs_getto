import streamlit as st
from streamlit import session_state as ss
import pandas as pd

st.title("Staff List")
st.write('Be sure to click "Save Changes" once you are done making changes.')
st.write("Don't click off of this tab until you are done and have hit save, or else your edits will not be saved!")
# df is getting edited
new_staff = st.data_editor(ss['staff'], num_rows='dynamic')

# Save changes 
if st.button('Save Changes'):
    if new_staff.equals(ss['staff']):
        st.error('No new changes were made')
    else:
        ss['staff'] = new_staff
        new_staff.to_excel('permanent_data/staff_directory.xlsx', index=False)
        st.success("Staff changes saved!")



# Staff upload section 
st.title("Upload New Staff List")
st.write("**Highly** suggest downloading a sample format and modifying it to your specifications.")
st.page_link("page_folder/formats_page.py", label="**Example formatts can be downloaded in the formatts section** (link)")
st.write("Follow the **exact** same formatting as in the image below. Column names must remain the same.")
st.write("Make sure everything is spelled correctly and that there are no extra spaces around the column names")
st.write("Make sure Lifeguard and Ropes consist of only TRUE and FALSE values.")
st.write("A staffer should have only 1 tag (Head Lifeguard, Leadership, etc.) or no tag at all.")
st.image("images/staff_example.png")
staff_file = st.file_uploader("Upload staff directory as excel file (.xlsx or .csv)", type=['.xlsx', '.csv'])

# Save uploaded file
if staff_file is not None and st.button("Submit File"):
    staff_df = pd.read_excel(staff_file).fillna("")
    staff_df[['Lifeguard', 'Ropes']] = staff_df[['Lifeguard', 'Ropes']].astype('bool')
    ss.staff = staff_df
    # Save in long term memory 
    staff_df.to_excel('permanent_data/staff_directory.xlsx', index=False)
    st.success("File saved successfully")