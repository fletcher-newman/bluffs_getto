import pandas as pd
import numpy as np
import streamlit as st
from streamlit import session_state as ss
from io import BytesIO
import hmac


def checkpass():
    """Asks for password input and returns false if password is incorect"""
    def password_entered():
        """Checks if entered password is correct"""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

def convert_excel(dataframe):
    """
    Convert a DataFrame to an Excel file in memory.
    """
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data


def tagcreate(save):
    ss[save] = False

def tagsave(save):
    ss[save] = True



def createGrid(sched, staff, week):
    # Create output dataframe
    grid = pd.DataFrame(sched['Activity'])

    # Create time list
    times = []
    for i in range(len(sched['Start'])):
        # Handle start time string
        s1 = int(sched['Start'][i] // 100)
        if s1 > 12:
            s1 -= 12
        s1 = str(s1)
        s2 = int(sched['Start'][i] % 100)
        add = ''
        if s2 == 0:
            add = '0'
        s2 = str(s2) + add
        start = s1 + ':' + s2

        # handle end time string
        e1 = int(sched['End'][i] // 100)
        if e1 > 12:
            e1 -= 12
        e1 = str(e1)
        e2 = int(sched['End'][i] % 100)
        add = ''
        if e2 == 0:
            add = '0'
        e2 = str(e2) + add
        end = e1 + ':' + e2

        times.append(start + '-' + end)

    grid['Time'] = times

    # Start assignment loop
        
    numStaff = len(staff)
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}

    for day in days:
        currDay = days[day]
        dayList = []

        for i in range(len(sched)):
            # Check if activity is scheduled that day
            if sched[currDay][i]:
                index = np.random.randint(0, len(staff))    # Sets random index to start checking staff 
                repeat = 0
                found = False
                noneFound = False

                # Loop through staff to see who can do it
                while not found:
                    repeat += 1

                    # If search finds no one avaible
                    if repeat > numStaff:
                        noneFound = True
                        found = True
                        continue

                    # Check if correct half
                    if staff['Half'][index] not in [half, 3]:
                        index = (index + 1) % numStaff
                        continue

                    # Check if they have been scheduled recently (1 hour buffer between when they get off and when they can start again)
                    if staff['prevDay'][index] == day:
                        if staff['prevTime'][index] + 1 > sched['Start'][i]:
                            index = (index + 1) % numStaff
                            continue

                    # Check if they meet the requirements
                    req = sched['Require'][i].split(',')
                    if '' not in req:
                        metReq = True
                        for crit in req:
                            crit = crit.strip()
                            if not staff[crit][index]:
                                metReq = False
                                break
                        if not metReq:
                            index = (index + 1) % numStaff
                            continue

                    # Passed all requirements, this is the one
                    found = True

                # Check if returned empty
                if noneFound:
                    dayList.append('NONE FOUND')

                # add staff to list and update their recent time attributes 
                else:
                    dayList.append(staff['Camp_name'][index])
                    staff.loc[index, 'prevDay'] = day
                    staff.loc[index, 'prevTime'] = sched['End'][i]

            else:
                dayList.append('')

        grid[currDay] = dayList  

    # Reset 
    staff['prevDay'] = np.zeros(len(staff['prevDay'])).astype(int)
    staff['prevTime'] = np.zeros(len(staff['prevTime'])).astype(int)
    return grid