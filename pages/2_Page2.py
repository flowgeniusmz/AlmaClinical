import streamlit as st
from functions import login as lg, pagesetup as ps, salesforce as sf
from streamlit_modal import Modal
import streamlit.components.v1 as components
import openai
from openai import OpenAI
import time
import uuid



#0. Page Config
st.set_page_config("AlmyAI", initial_sidebar_state="collapsed", layout="wide")

#1. Login and Page Setup
if lg.check_authentication():
    ps.set_title("AlmyAI", "Clinical")
    ps.set_page_overview("Clinical Assistant", "**Clinical Assistant** is an AI-based assistant trained to interact with the Alma Clinical team.")

    container0 = st.container()
    with container0:
        email = st.text_input("Enter your Salesforce email", key="tiEmail")
        sUserId = sf.get_sfUserID(email)
        st.write(sUserId)

            
