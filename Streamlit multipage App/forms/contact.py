import streamlit as st 

import re

import requests

#a link if I would like to save the contact data the clients say to in my project like in an json file
WEBHBOOK_URL = ""

#code to check email validity
def is_valid_email(email):
    #basic regex pattern for email validation
    email_pattern = r"^[a-zA-ZO-9_.+-]+@[a-zA-ZO-9_.+-]+\.[a-zA-ZO-9_.+-] + $"
    return re.match(email_pattern, email) is not None



def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name ")
        email = st.text_input('Email adress')
        message = st.text_area('Your Message: ')
        submit_button = st.form_submit_button('submit')

        if submit_button: 
            st.success('Message succesfuly sent! ')