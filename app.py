import streamlit as st
import requests
from auth_page import auth_view
from documents_chat_page import document_chat_view
from home_page import home_view


LOGGED_IN = True

st.set_page_config(page_title="Data Analysis", page_icon="👨‍💻")
user_authenticated = True

if LOGGED_IN == True:
    menu = st.sidebar.selectbox("Choose an option", ["Home","Chat with Documents", "Pandas Dataframe","Pandas AI Analysis","Lida Analysis","Lida Q&A Analysis"])
    if menu == "Home":
        home_view()
    elif menu == "Chat with Documents":
        document_chat_view()
   
    

