#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pickle
import pandas as pd

# Charger le modèle pré-entraîné
model = pickle.load(open('model.pkl', 'rb'))

# Définir une fonction pour la classification
def classify(num):
    if num > 0:
        return '1 : Client will exit'
    else:
        return '0 : Client will not exit'

# Créer l'interface utilisateur avec Streamlit
def main():
    html_temp = """
    <style>
    .appview-container .main .block-container{{
        max-width: 800px;
    }}
    .reportview-container .main {{
        color: black;
        background-color: white;
    }}
    </style>
    <div style="background-color:teal ;padding:10px">
    <h3 style="font-size:18pt;color:white;text-align:center;">Churn Prediction (0 : Will Not Exit | 1 : Will Exit)</h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.title("Churn Prediction for Bank Customers")
    
    # Collect user input for model features
    Surname = st.text_input('Surname')
    CreditScore = st.slider('Credit Score', 350, 850, step=1)
    Geography = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Age = st.slider('Age', 18, 92, step=1)
    Tenure = st.slider('Tenure (years)', 0, 10, step=1)
    Balance = st.slider('Balance', 0.0, 250000.0, step=1000.0)
    NumOfProducts = st.slider('Number of Products', 1, 4, step=1)
    HasCrCard = st.selectbox('Has Credit Card', [0, 1])
    IsActiveMember = st.selectbox('Is Active Member', [0, 1])
    EstimatedSalary = st.slider('Estimated Salary', 0.0, 200000.0, step=1000.0)
    
    # Transform categorical features into numerical values
    Geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
    Gender_map = {'Male': 0, 'Female': 1}
    
    inputs = [[CreditScore, Geography_map[Geography], Gender_map[Gender], Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]]
    
    if st.button('Classify'):
        prediction = model.predict(inputs)
        st.success(f'Surname: {Surname}, Prediction: {classify(prediction[0])}')

        if __name__ == '__main__':
            main()


# In[ ]:




