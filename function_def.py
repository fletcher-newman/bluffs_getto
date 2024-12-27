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



def createGrid(sched, staff):
    # Create output dataframe
    grid = pd.DataFrame(sched['Activity'])

    staff["prevTime"] = 0
    staff["prevDay"] = 0

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
        
    numStaff = len(ss.roster)
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
    names = list(ss.roster.keys())

    for day in days:
        currDay = days[day]
        dayList = []

        for i in range(len(sched)):
            # Check if activity is scheduled that day
            if sched[currDay][i]:
                index = np.random.randint(0, numStaff)    # Sets random index to start checking staff 
                repeat = 0
                found = False
                noneFound = False

                # Loop through staff to see who can do it
                while not found:
                    name = names[index]
                    nameData = staff.query('Camp_name == @name')
                    repeat += 1

                    # If search finds no one avaible
                    if repeat > numStaff:
                        noneFound = True
                        found = True
                        continue

                    # Check if they have been scheduled recently (1 hour buffer between when they get off and when they can start again)
                    if nameData['prevDay'][nameData.index[0]] == day:
                        if nameData['prevTime'][nameData.index[0]] + 1 > sched['Start'][i]:
                            index = (index + 1) % numStaff
                            continue

                    # If they are kcrew, check if they have a shift durring that time (ignore if it is sunday)
                    # ASSUMING AM'ER: 600-1200 (6am-12pm), AFTIE: 1330-1800 (1:30pm-6:00pm)
                    if name in ss.kcrew and day != 0:
                        # Check morning 
                        if ss.kcrew[name] == "AM'er" and sched["Start"][i] < 1300:
                            index = (index + 1) % numStaff
                            continue
                        elif ss.kcrew[name] == "Aftie" and ((sched["Start"] > 1300 and sched["Start"] < 1830) or (sched["End"] > 1300 and sched["End"] < 1830)):
                            index = (index + 1) % numStaff
                            continue
                            

                    # Check if they have a 1on1
                    if ss.roster[name][1]:
                        index = (index + 1) % numStaff
                        continue

                    # Check if they meet the requirements
                    req = sched['Require'][i].split(',')
                    for w in range(len(req)):
                        req[w] = req[w].strip()

                    # Check if leadership can be skipped
                    if ("Leadership" not in req) and ss.roster[name][0] == "Leadership":
                        index = (index + 1) % numStaff
                        continue
                    
                    metReq = True
                    for crit in req:
                        # Must check the roster dict to see if they are workcrew
                        if crit == "Non-program" and ss.roster[name][0] in ["Impact", "Crew", "Cove"]:
                            metReq = False
                            break
                        # Check gender
                        elif crit in ["Male", "Female"] and nameData['Gender'][nameData.index[0]] != crit:
                            metReq = False
                            break
                        # Check leadership
                        elif (crit == "Leadership") and (ss.roster[name][0] != "Leadership"):
                            metReq = False
                            break
                        # Check certification 
                        elif crit in ["Ropes", "Lifeguard"] and not nameData[crit][nameData.index[0]]:
                            metReq = False
                            break
                    if not metReq:
                        index = (index + 1) % numStaff
                        continue

                    # Check if they have any tags that make them ineligable
                    # Still need to check sound/projects and media
                    if "Leadership" not in req or ss.roster[name][0] not in ["Impact", "Crew", "Cove"]:
                        tag = nameData["Tag"][nameData.index[0]].strip()
                        if tag in ["Health Assistant", "Head Lifeguard", "Camp Store"]:
                            index = (index + 1) % numStaff
                            continue
                            


                    # Passed all requirements, this is the one
                    found = True

                # Check if returned empty
                if noneFound:
                    dayList.append('NONE FOUND')

                # add staff to list and update their recent time attributes 
                else:
                    dayList.append(name + " " + str(ss.roster[name][0]) + " Lifeguard:" + str(nameData["Lifeguard"][nameData.index[0]]) + " Ropes:" + str(nameData["Ropes"][nameData.index[0]]))
                    staff.loc[nameData.index[0], 'prevDay'] = day
                    staff.loc[nameData.index[0], 'prevTime'] = sched['End'][i]

            else:
                dayList.append('')

        grid[currDay] = dayList  

    # Reset 
    del staff['prevDay'] 
    del staff['prevTime'] 
    return grid


def trans_kcrew(kcrew_df):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    shifts = ["AM'er", "Aftie", "Wickie", "O'fer"]
    for day in days:
        shift = ""
        dayList = list(kcrew_df[day])
        for i in range(len(dayList)):
            if dayList[i] in shifts:
                shift = dayList[i]
                continue
            elif dayList[i] not in list(ss.staff["Camp_name"]):
                st.error(f"{dayList[i]} is not in the staff directory")
                continue
            else:
                if dayList[i] not in ss.kcrew:
                    ss.kcrew[dayList[i]] = {}
                ss.kcrew[dayList[i]][day] = shift
        
