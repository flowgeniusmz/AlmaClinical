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

@st.cache_data
def get_all_clinical_training():
    #query = f"SELECT Account__c, Asset__c, Assigned_Email__c, Install_Date__c, Status__c, Assigned__c, Booked_to_Training_Complete__c, Booked_Date__c, City__c, Contact__c, Contact_Email__c, Contact_Phone__c, Days_from_installation__c, Initial_Call_Date__c, Install_to_Training_Complete__c, Opportunity__c, OwnerId, Product_From_Asset__c, Product__c, Sales_rep__c, Scheduler__c, Ship_Date__c, State_Province__c, Status__c, Training_End_Date__c, Training_Length__c, Training_Type__c FROM Clinical_Trainings__c WHERE Subsidiary__c = 'Alma Lasers , Inc.'"
  query = f"SELECT Account__c, Asset__c, Assigned_Email__c, Install_Date__c, Status__c FROM Clinical_Trainings__c WHERE Subsidiary__c = 'Alma Lasers , Inc.'"  
  data = sf.query(query)
    records = data['records']

    # Extracting data from each record
    tdata = []
    for record in records:
        row = {
            'Account__c': record.get('Account__c', None),
            'Asset__c': record.get('Asset__c', None),
            'Assigned_Email__c': record.get('Assigned_Email__c', None),
            'Install_Date__c': record.get('Install_Date__c', None),
            'Status__c': record.get('Status__c', None),
            'Assigned__c': record.get('Assigned__c', None),
            'Booked_to_Training_Complete__c': record.get('Booked_to_Training_Complete__c', None),
            'Booked_Date__c': record.get('Booked_Date__c', None),
            'City__c': record.get('City__c', None),
            'Contact__c': record.get('Contact__c', None),
            'Contact_Email__c': record.get('Contact_Email__c', None),
            'Contact_Phone__c': record.get('Contact_Phone__c', None),
            'Days_from_installation__c': record.get('Days_from_installation__c', None),
            'Initial_Call_Date__c': record.get('Initial_Call_Date__c', None),
            'Install_to_Training_Complete__c': record.get('Install_to_Training_Complete__c', None),
            'Opportunity__c': record.get('Opportunity__c', None),
            'OwnerId': record.get('OwnerId', None),
            'Product_From_Asset__c': record.get('Product_From_Asset__c', None),
            'Product__c': record.get('Product__c', None),
            'Sales_rep__c': record.get('Sales_rep__c', None),
            'Scheduler__c': record.get('Scheduler__c', None),
            'Ship_Date__c': record.get('Ship_Date__c', None),
            'State_Province__c': record.get('State_Province__c', None),
            'Status__c': record.get('Status__c', None),
            'Training_End_Date__c': record.get('Training_End_Date__c', None),
            'Training_Length__c': record.get('Training_Length__c', None),
            'Training_Type__c': record.get('Training_Type__c', None)
        }
        tdata.append(row)

    # Creating a DataFrame from the list of dictionaries
    df = pd.DataFrame(tdata)

    return df

    
  

