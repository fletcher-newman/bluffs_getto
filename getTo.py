import pandas as pd
import streamlit as st
from streamlit import session_state as ss
from function_def import checkpass

#Checks for correct password before continuing to the rest of the app
if not checkpass():
    st.stop()


# Import files and convert columns to bool
sched = pd.read_excel('getto_format.xlsx')
staff = pd.read_excel('staff_getto.xlsx')
staff[['Male', 'Female', 'Lifegaurd', 'Ropes', 'Workcrew', 'OneOnOne', 'Leadership', 'Boatie']] = staff[['Male', 'Female', 'Lifegaurd', 'Ropes', 'Workcrew', 'OneOnOne', 'Leadership', 'Boatie']].astype('bool')
sched[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']] = sched[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].astype(bool)
sched = sched.fillna('')



#put global variables in the session state
if 'sched' not in ss:
    ss.sched = sched
if 'staff' not in ss:
    ss['staff'] = staff
if 'bsave_tag' not in ss:
    ss.bsave_tag = False
if 'grid' not in ss:
    ss.grid = None
if 'week' not in ss:
    ss.week = 0



def info_page():
    st.title("How to use the get-to grid creator")


def contact_page():
    st.title("Contact info")
    st.markdown("**If any problems arise or you have any questions, please contact:**")
    st.write("Fletcher Newman")
    st.write("Email (prefered): fletcht13@gmail.com")
    st.write("Phone: 214-949-7274")
    st.write("This application was created by Fletcher Newman in November of 2024 for Pine Cove Bluffs")


pages = {
    'Get To Grid Creator': [
        st.Page('sched_page.py', title="Edit Grid Schedule"),
        st.Page('staff_page.py', title="Edit Staff List"),
        st.Page("createGrid_page.py", title="Create Grid"),
        st.Page("editGrid_page.py", title="Edit Grid"),
    ],
    'Information': [
        st.Page(info_page, title= "Instructions"),
        st.Page(contact_page, title="Contact")

    ]
}

pg = st.navigation(pages)
pg.run()
