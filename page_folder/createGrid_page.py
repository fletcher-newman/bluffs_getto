import numpy as np
import streamlit as st
from streamlit import session_state as ss
from streamlit_js_eval import streamlit_js_eval
from function_def import tagcreate, tagsave, createGrid


st.title("Create Get-To Grid")

weeks = np.arange(1, 11) 
if not ss.bsave_tag:
    ss.week = st.selectbox("Select week", weeks, index=None, placeholder='week')

if ss.week in weeks:
    #Add create button (initiates getto algorithm)
    label = "Create grid for week " + str(ss.week)
    create_button = st.button(label, on_click=tagcreate, args=('bsave_tag',))

    # Once button is cliked, grid algorithm runs and grid is returned
    if create_button:
        if len(ss.roster) == 0:
            st.error("The weekly roster is currently empty.")
        else:
            ss.grid = createGrid(ss['sched'], ss['staff'])
            st.dataframe(ss.grid)  # Displays grid without editability

            # Create save button
            st.button("Save Grid", on_click=tagsave, args=('bsave_tag',))


    if ss.bsave_tag:
            file_name = 'Grids/GetToGrid_Week' + str(ss.week) + '.xlsx'
            ss.grid.to_excel(file_name)
            st.dataframe(ss.grid)
            st.success("Get-to grid saved in 'Grid' folder!")
            st.write("You can now edit this grid in the 'Edit Grid' tab")
            st.write("Click reset to create another grid")


if st.button("Reset"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")