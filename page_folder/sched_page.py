import streamlit as st
from streamlit import session_state as ss

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
        new_sched.to_excel('getto_format.xlsx', index=False)
        st.success("Schedule changes saved!")