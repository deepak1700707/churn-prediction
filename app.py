import pickle
import streamlit as st
import pandas as pd
import numpy as np

model = pickle.load(open('Customer_churn_model.sav', 'rb'))
data = []
def prediction(age,creditscore,balance,estimated_salary,Gender,Geography,HasCrCard,IsActiveMember,Tenure,NumOfProducts):
    data = [creditscore,age,Tenure,balance,NumOfProducts]
    if HasCrCard == 'Yes':
        data.append(1)
    else:
        data.append(0)
    if IsActiveMember == 'Yes':
        data.append(1)
    else:
        data.append(0)
    data.append(estimated_salary)
    if (Geography == "France"):
        data.extend([0,0])
    elif (Geography == "Spain"):
        data.extend([0,1])
    elif (Geography == "Germany"):
        data.extend([1,0])
    if (Gender == "Male"):
        data.append(1)
    else:
        data.append(0)
    ans = [data]
    prediction = model.predict(ans)
    return prediction



html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Customer Churn Prediction ML App </h1>
    </div>
    """

# this line allows us to display the front end aspects we have
# defined in the above code
st.markdown(html_temp, unsafe_allow_html=True)


CreditScore = st.number_input("CreditScore")

Geography = st.selectbox(
    'Select Geography',
    ('France', 'Spain','Germany'))

HasCrCard = st.selectbox(
    'Select HasCrCard',
    ('Yes', 'No'))

IsActiveMember = st.selectbox(
    'Select IsActiveMember',
    ('Yes', 'No'))

Gender = st.selectbox(
    'Select Gender',
    ('Male', 'Female'))
Balance = st.number_input("Balance")
EstimatedSalary = st.number_input("EstimatedSalary")
Age = st.slider('Age ', 18, 92, 18)
Tenure = st.slider('Tenure ', 0, 10, 0)
NumOfProducts = st.slider('NumOfProducts ', 1, 4, 1)



if st.button("Predict"):
    print(data)
    result = prediction(Age,CreditScore,Balance,EstimatedSalary,Gender,Geography,HasCrCard,IsActiveMember,Tenure,NumOfProducts)
    if result == 1:
        st.success('Your prediction --> {}'.format(" Customer Will Leave"))
    else:
        st.success('Your prediction --> {}'.format(" Customer Will Not Leave"))
