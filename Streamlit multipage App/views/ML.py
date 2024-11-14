import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load the dataset
df = pd.read_csv("D:\My Projects\Final Project\credit_train.csv", na_values=['x'])
df.drop(columns=['Customer_ID', 'ID', 'Unnamed: 0'], inplace=True)

# Load the saved KNN pipeline
with open("D:\My Projects\Final Project\pipeline_Knn.pkl", 'rb') as file:
    pipeline_knn = joblib.load(file)
    
    model_features = ['Age', 'Amount_invested_monthly', 'Delay_from_due_date', 'Monthly_Balance', 'Num_of_Delayed_Payment']

    numerical_cols = ['Monthly_Inhand_Salary', 'Delay_from_due_date', 'Num_Credit_Inquiries',
                      'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Total_EMI_per_month',
                      'Amount_invested_monthly', 'Monthly_Balance', 'Credit_Score', 'Num_Bank_Accounts']

     # Input fields
    # Collect user input
    age = st.number_input("Age", min_value=0)
    amount_invested_monthly = st.number_input("Amount Invested Monthly", min_value=0)
    delay_from_due_date = st.number_input("Delay from Due Date", min_value=0)
    monthly_balance = st.number_input("Monthly Balance", min_value=0)
    num_of_delayed_payment = st.number_input("Number of Delayed Payments", min_value=0)
    annual_income = st.number_input('Annual Income', min_value=0.0, value=0.0)
    monthly_salary = st.number_input('Monthly Inhand Salary', min_value=0.0, value=0.0)
    num_bank_accounts = st.number_input('Number of Bank Accounts', min_value=0, value=0)
    num_credit_cards = st.number_input('Number of Credit Cards', min_value=0, value=0)
    interest_rate = st.number_input('Interest Rate', min_value=0, value=0)
    num_of_loans = st.number_input('Number of Loans', min_value=0, value=0)
    changed_credit_limit = st.number_input('Changed Credit Limit', min_value=0, value=0)
    num_credit_inquiries = st.number_input('Number of Credit Inquiries', min_value=0, value=0)
    credit_mix = st.number_input('Credit Mix', min_value=0, value=0)
    outstanding_debt = st.number_input('Outstanding Debt', min_value=0.0, value=0.0)
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0.0, max_value=1.0, value=0.0)

    # Button to make prediction
    if st.button('Predict Credit Score'):
        # Prepare input data
        input_data = pd.DataFrame({
            'Annual_Income': [annual_income],
            'Monthly_Inhand_Salary': [monthly_salary],
            'Num_Bank_Accounts': [num_bank_accounts],
            'Num_Credit_Card': [num_credit_cards],
            'Interest_Rate': [interest_rate],
            'Num_of_Loan': [num_of_loans],
            'Changed_Credit_Limit': [changed_credit_limit],
            'Num_Credit_Inquiries': [num_credit_inquiries],
            'Credit_Mix': [credit_mix],
            'Outstanding_Debt': [outstanding_debt],
            'Credit_Utilization_Ratio': [credit_utilization_ratio],
        })

        # Predict the credit score
        prediction = pipeline_knn.predict(input_data)

        # Show the prediction
        st.write(f'Predicted Credit Score: {prediction[0]}')