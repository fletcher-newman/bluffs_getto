import streamlit as st

st.title("Format downloads")
st.write("Here is a list of formats that work with this app")
st.write("You are free to download these formats and edit them to your specifications")
st.write("Do not change the names of the columns and try and keep everything the same except for the names/values in the cells that you need to change.")
st.write(" ")


# SCHEDULE FORMAT
st.write("**Get-to Schedule Format**")
st.image("images/sched_example.png")
getto_path = "formats/getto_format_download.xlsx"
# Read the Excel file in binary mode
with open(getto_path, "rb") as file:
    getto_data = file.read()
# Create the download button
st.download_button(
    label="Download Schedule File",
    data=getto_data,
    file_name="getto_format.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.write(" ")


# STAFF DIRECTORY FORMAT
st.write("**Staff Directory Format**")
st.image("images/staff_example.png")
staff_path = "formats/staff_format_download.xlsx"
# Read the Excel file in binary mode
with open(staff_path, "rb") as file:
    staff_data = file.read()
# Create the download button
st.download_button(
    label="Download Staff File",
    data=staff_data,
    file_name="staff_format.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.write(" ")

# ROSTER FORMAT
st.write("**Weekly Roster Format**")
st.image("images/roster_example.png")
roster_path = "formats/roster_format_download.xlsx"
# Read the Excel file in binary mode
with open(roster_path, "rb") as file:
    roster_data = file.read()
# Create the download button
st.download_button(
    label="Download Roster File",
    data=roster_data,
    file_name="roster_format.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.write(" ")

# KCREW FORMAT
st.write("**Weekly K-crew Format**")
st.image("images/kcrew_example.png")
kcrew_path = "formats/kcrew_format_download.xlsx"
# Read the Excel file in binary mode
with open(kcrew_path, "rb") as file:
    kcrew_data = file.read()
# Create the download button
st.download_button(
    label="Download K-crew File",
    data=kcrew_data,
    file_name="roster_format.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)