import pandas as pd
import streamlit as st
from streamlit import session_state as ss
from function_def import checkpass

#Checks for correct password before continuing to the rest of the app
if not checkpass():
    st.stop()




#put global variables in the session state
if 'sched' not in ss:
    sched = pd.read_excel('permanent_data/get_to_schedule.xlsx')
    sched[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']] = sched[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].astype(bool)
    sched = sched.fillna('')
    ss.sched = sched
if 'staff' not in ss:
    staff = pd.read_excel('permanent_data/staff_directory.xlsx')
    staff[['Lifeguard', 'Ropes']] = staff[['Lifeguard', 'Ropes']].astype('bool')
    staff = staff.fillna("")
    ss.staff = staff
if 'bsave_tag' not in ss:
    ss.bsave_tag = False
if 'grid' not in ss:
    ss.grid = None
if 'week' not in ss:
    ss.week = 0
if 'roster' not in ss:
    # Roster is dictionary with camp name as key and a list of which program they are in and bool if they have a one on one.
    # {CampName: [Program, OneOnOne?(T/F)]}
    # Go ahead and put in leadership
    leadership_df = ss.staff[ss.staff["Tag"] == "Leadership"]
    ss.roster = {row["Camp_name"]: ["Leadership", False] for _, row in leadership_df.iterrows()}
if 'kcrew' not in ss:
    # kcrew is nested dict with campname as outer key and day as inner key and what their assignment was (am'er, afttie, wickie, o'fer) for that day
    # Only one assignment per person per day
    ss.kcrew = {}

def info_page():
    st.title("How to use the get-to grid creator")


def contact_page():
    st.title("Contact info")
    st.markdown("**If any problems arise or you have any questions, please contact:**")
    st.write("Fletcher Newman")
    st.write("Email (prefered): fletcht13@gmail.com")
    st.write("Phone: 214-949-7274")
    st.write("This application was created by Fletcher Newman in November of 2024 for Pine Cove Bluffs")
    st.write(ss.impact)


pages = {
    'Edit Weekly Staff Roster': [
        st.Page("page_folder/weekly_edits/manual_roster_page.py", title="Manual Input"),
        st.Page("page_folder/weekly_edits/upload_roster_page.py", title="File Upload"),
        st.Page("page_folder/weekly_edits/kcrew_page.py", title="K-crew Schedule Upload")
    ],
    'Edit Full Summer Data': [
        st.Page('page_folder/sched_page.py', title="Edit Grid Schedule"),
        st.Page('page_folder/staff_page.py', title="Edit Staff List"),
        st.Page("page_folder/editGrid_page.py", title="Edit Grid"),
    ],
    'Get To Grid Creator': [
        st.Page("page_folder/createGrid_page.py", title="Create Grid")
    ],
    'Information': [
        st.Page(info_page, title= "Instructions"),
        st.Page(contact_page, title="Contact"),
        st.Page("page_folder/formats_page.py", title="Download Formats")

    ]
}

pg = st.navigation(pages)
pg.run()
