import pandas as pd
import numpy as np
import streamlit as st
from streamlit import session_state as ss
from function_def import convert_excel

st.title('Edit Grid')
weeks = np.arange(1, 11) 
week = st.selectbox("Select the week you would like to edit", weeks, index=None, placeholder='week')

if week in weeks:
    try:
        # Opens grid file from folder 
        fileName = 'Grids/GetToGrid_Week' + str(week) + '.xlsx'
        edit_grid = pd.read_excel(fileName)

        # Grid displayed and can be edited
        new_edit_grid = st.data_editor(edit_grid)
        st.markdown("**You must hit save for changes to become permanent**")

        # Auto save after each change
        save_edit_button = st.button('Save')
        if save_edit_button:
            if new_edit_grid.equals(edit_grid):
                st.error('No changes have been made')
            else:
                new_edit_grid.to_excel(fileName, index=False)
                st.success('File saved successfuly')

        # Create download button to download file as .xlsx
        excel_file = convert_excel(new_edit_grid)
        download_name = 'GetToGrid_Week' + str(week) + '.xlsx'
        download_button = st.download_button(
                label="Download File (excel)",
                data=excel_file,
                file_name=download_name,
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        if download_button:
            new_edit_grid.to_excel(fileName, index=False)
            st.success("File successfuly downloaded")

    except FileNotFoundError:
        message = 'There has not been a grid created for week ' + str(week) + '. Please create a grid for week ' + str(week) + ' or select another week.'
        st.error(message)



