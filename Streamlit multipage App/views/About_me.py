import streamlit as st 

from forms.contact import contact_form


st.experimental_dialog('Contact Me')
def show_contact_form():
    contact_form()

# ---- Hero section ----
col1,col2 = st.columns(2,gap = 'small', vertical_alignment ='center')
with col1:
    st.image('D:\CDSP\Final_Project\Streamlit multipage App\Assets\IMG-20220824-WA0012.jpg',width=230)
with col2:
    st.title('Omar Saad',anchor=False)
    st.write(
        'I am a Business Analytics graduate currently working as a freelancer in the tech industry. I am eager to utilize my skills and passion to contribute to innovative projects. Technologically adept, I bring the latest academic knowledge, hands-on experience with office technology programs, advanced computer skills, and strong analytical abilities. With a positive attitude and high motivation, I am committed to continuous learning and applying new skills to drive impactful results.'
             )
    if st.button ('Contact me'):
        show_contact_form()

st.write("\n")
st.subheader('Experience * Qualifications',anchor=False)
st.write(
    """
    - 2 Weeks  Hands on experinece Finance Internship in Petronefertiti Co. 2023
    - 6 months Digital Transformation Internship in attijirwafa Bank 2024 - Present
    - professional athlete with over 11 medals claimed in (Swimming & Gymnastics) 
    """
)       

st.write('\n')
st.subheader('Tehnical Skills',anchor=False)
st.write(
    """
    - Python(pandas,numpy,matplotlib,sklearn,seaborn)
    - Web Scraping
    - Ms Office
    - PowerBi
    - EDA Explotary Data Analysis
    - Ideas system (oracle sub_system)
    - AP Accounts payable 
    """
)

st.write('\n')
st.subheader('Languages',anchor=False)
st.write(
    """
    - Arabic (mother tongue)
    - English C1
    - French (Delf B1)
    """
)

st.write('\n')
st.subheader('Soft skills',anchor=False)
st.write(
    """
    - Presentation
    - Negotiation skills
    - Innovative
    - Teamwork
    - Attention to detail
    - Complex problem solver
    """
)