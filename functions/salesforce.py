import streamlit as st
from simple_salesforce import Salesforce
import pandas as pd
from collections import OrderedDict

sUN = st.secrets.SALESFORCE_USERNAME
sPW = st.secrets.SALESFORCE_CRED
sTK = st.secrets.SALESFORCE_TOKEN

sf = Salesforce(username = sUN, password = sPW, security_token = sTK)

def get_sfUserID(varEmail):

  query = f"SELECT Id FROM User WHERE Username = '{varEmail}'"
  data = sf.query(query)
  userid = data['records'][0]['Id']
  return userid

