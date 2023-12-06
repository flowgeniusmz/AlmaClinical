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

def get_trainings(varUser):
  query = f"SELECT Account__c, Asset__c, Assigned_Email__c, Install_Date__c, Status__c FROM Clinical_Trainings__c WHERE Assigned_Email__c = '{varUser}'"  
  data = sf.query(query)
  records = data['records']

  # Create a list to store the data
  training_data = []

  # Loop through each record
  for record in records:
      account = record['Account__c']
      asset = record['Asset__c']
      assigned_email = record['Assigned_Email__c']
      install_date = record['Install_Date__c']
      status = record['Status__c']

      # Add the data to the list
      training_data.append([account, asset, assigned_email, install_date, status])

  # Create a DataFrame from the list
  df = pd.DataFrame(training_data, columns=['Account', 'Asset', 'Assigned Email', 'Install Date', 'Status'])

  return df
    
