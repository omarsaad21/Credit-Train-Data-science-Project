import streamlit as st 



# --- Page Setup---
about_page=st.Page(
    page="views/About_me.py",
    title='About me',
    icon = ":material/account_circle:",
    default=True,
)
Project_1_page = st.Page(
    page="views/Data_Analysis.py",
    title="Data Analysis",
    icon=':material/thumb_up:',
)
project_2_page=st.Page(
    page='views/ML.py',
    title="Machine Learning",
    icon=':material/smart_toy:',
)
#-----Navigation Setup without Sections----
#pg=st.navigation(pages=[about_page,Project_1_page,project_2_page])

# -----Navigation setup with actions-----
pg=st.navigation(
    {
        'info':[about_page],
        'Credit Train':[Project_1_page,project_2_page],
    }
)

#---Running navigation---
pg.run()
