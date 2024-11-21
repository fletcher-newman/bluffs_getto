import streamlit as st
from streamlit import session_state as ss

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
        new_staff.to_excel('staff_getto.xlsx', index=False)
        st.success("Staff changes saved!")