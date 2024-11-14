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


 # Drop any specific outliers if needed
    df = df.drop(54739, axis=0)

    # Categorical column visualizations
    categorical_cols = ['Month', 'Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour']
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x=col)
        plt.title(f'Count of {col}')
        plt.xticks(rotation=45)
        st.pyplot(plt)

    # Pie chart for Occupation
    st.subheader("Occupation Distribution")
    plt.figure(figsize=(10, 5))
    df["Occupation"].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Occupation Distribution')
    st.pyplot(plt)

    

    # Bar chart for Credit Mix
    st.subheader("Credit Mix Distribution")
    plt.figure(figsize=(10, 5))
    df["Credit_Mix"].value_counts().plot.bar()
    plt.title('Credit Mix Distribution')
    st.pyplot(plt)

    # Boxplot: Credit Score vs Monthly Inhand Salary
    st.subheader("Credit Score vs Monthly Inhand Salary")
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='Credit_Score', y='Monthly_Inhand_Salary', data=df)
    st.pyplot(plt)

    # Bar plot: Monthly Inhand Salary vs Outstanding Debt (Top 10)
    st.subheader("Monthly Inhand Salary vs Outstanding Debt (Top 10)")
    plt.figure(figsize=(10, 5))
    df[["Monthly_Inhand_Salary", "Outstanding_Debt"]].head(10).plot.bar()
    plt.title('Monthly Inhand Salary vs Outstanding Debt')
    st.pyplot(plt)

    # Barplot: Credit Score vs Credit Mix
    st.subheader("Credit Score vs Credit Mix")
    grouped_data = df.groupby('Credit_Mix')['Credit_Score'].mean()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=grouped_data.index, y=grouped_data)
    plt.xlabel('Credit Mix')
    plt.ylabel('Credit Score')
    plt.title('Credit Score vs Credit Mix')
    st.pyplot(plt)

    # Heatmap of correlations
    st.subheader("Correlation Heatmap")
    heatmap = df.select_dtypes(exclude='object').corr()
    plt.figure(figsize=(10, 5))
    sns.heatmap(heatmap, annot=True)
    st.pyplot(plt)
