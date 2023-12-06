import streamlit as st
from functions import login as lg, pagesetup as ps
from streamlit_modal import Modal
import streamlit.components.v1 as components


#0. Page Config
st.set_page_config("AlmyAI", initial_sidebar_state="collapsed", layout="wide")

#1. Login and Page Setup
if lg.check_authentication():
    ps.set_title("AlmyAI", "Clinical")
    ps.set_page_overview("Overview", "**Clinical Assistant** puts AI in the hands of Alma Clinical.")

    
