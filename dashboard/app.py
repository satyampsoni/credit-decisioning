import streamlit as st
import pandas as pd
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np

st.set_page_config(layout="centered", page_title="Credit Decisions")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Credit Decisioning", "Project Overview"])

# Page 1: Credit Decisioning
if page == "Credit Decisioning":
    st.markdown("<h1>Credit Decisioning</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Enter Applicant Details Below</h2>", unsafe_allow_html=True)

    st.markdown("<p class='quote'>“This is a project of Google Summer of Code@OpenSUSE” </p>", unsafe_allow_html=True)

    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<div class='form-row'>", unsafe_allow_html=True)

    gender = st.selectbox('Gender', ['Male', 'Female'])
    married = st.selectbox('Married', ['Yes', 'No'])
    education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
    applicant_income = st.text_input('Applicant Income *', placeholder='Enter applicant income in US dollars')
    coapplicant_income = st.text_input('Coapplicant Income *', placeholder='Enter coapplicant income in us dollars')
    loan_amount = st.text_input('Loan Amount *', placeholder='Enter loan amount in us dollars')
    loan_amount_term_months = st.text_input('Loan Amount Term (Months) *', placeholder='Enter loan term in months')
    credit_history = st.selectbox('Credit History *', ['0', '1'])
    property_area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'])

    # Validation for empty inputs
    if applicant_income and coapplicant_income and loan_amount and loan_amount_term_months:
        applicant_income = float(applicant_income)
        coapplicant_income = float(coapplicant_income)
        loan_amount = float(loan_amount)
        loan_amount_term_days = float(loan_amount_term_months) * 30  # Convert months to days
        
        label_encoder = preprocessing.LabelEncoder()
        gender = label_encoder.fit_transform([gender])[0]
        married = label_encoder.fit_transform([married])[0]
        education = label_encoder.fit_transform([education])[0]
        self_employed = label_encoder.fit_transform([self_employed])[0]
        property_area = label_encoder.fit_transform([property_area])[0]


        scaler = StandardScaler()
        applicant_income = scaler.fit_transform(np.array(applicant_income).reshape(-1, 1)).flatten()[0]
        coapplicant_income = scaler.fit_transform(np.array(coapplicant_income).reshape(-1, 1)).flatten()[0]
        loan_amount = scaler.fit_transform(np.array(loan_amount).reshape(-1, 1)).flatten()[0]
        loan_amount_term_days = scaler.fit_transform(np.array(loan_amount_term_days).reshape(-1, 1)).flatten()[0]

        final_input = np.array([gender, married, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term_days, credit_history, property_area]).reshape(1, -1)

        if st.button("Predict"): 
            with open("../model/model.pkl", "rb") as f:
                model = pickle.load(f)
            output = model.predict(final_input)
            if output[0] == 0:
                st.write("Please try again later after sometime")
            elif output[0] == 1:
                st.write("You are eligible")
    else:
        st.warning("Please fill in all the required fields before submitting the form.")

# Page 2: Project Overview
elif page == "Project Overview":
    st.markdown("<h1>Project Overview</h1>", unsafe_allow_html=True)
    st.markdown("""
    <h2>Motivation</h2>
    <p>The finance industry relies on data analytics, including machine learning (ML), to describe, predict, and improve performance. Data can be anywhere and is not always found in the core data center. Increasingly, the data needed by organizations is located at the edge - in branch sites and even in mobile and IoT devices. Moving data from edge to core introduces latency, costs, and security risks.</p>
    <p>The goal is to empower individuals to make informed loan decisions, transforming the often daunting process into something accessible and user-friendly.</p>

    <h2>Edge Analytics in Finance Vertical</h2>
    <p>The project is designed to develop an open-source application that leverages distributed edge-core-cloud infrastructure specifically for assessing loan applications. By utilizing a cloud-native approach to containerization, the project aims to enhance the speed and accuracy of credit decisions, enabling financial institutions to make informed lending decisions based on real-time analytics. This project is part of <strong>Google Summer of Code</strong>, and I would like to thank my mentors <strong>Bryan Gartner, Navin Chandra, Terry Smith,</strong> and <strong>Ann Davis</strong> for their consistent support and belief in me.</p>

    <h2>Objectives</h2>
    <ul>
        <li>To create a scalable microservice architecture for processing loan application data.</li>
        <li>To implement edge computing techniques that allow for faster data processing and analytics closer to where the data is generated.</li>
        <li>To provide a toolkit for credit analysts and loan officers to evaluate loan applications efficiently, ensuring a fair and data-driven decision-making process.</li>
    </ul>

    <h2>Key Features</h2>
    <ul>
        <li><strong>User-Friendly Interface</strong>: A web-based interface that allows users to input loan application details easily.</li>
        <li><strong>Real-Time Credit Decisions</strong>: The application processes inputs and provides immediate feedback on loan eligibility using predictive models.</li>
        <li><strong>Data-Driven Insights</strong>: The system analyzes historical data and current market conditions to inform credit decisions.</li>
        <li><strong>Open Source</strong>: The project includes a GitHub repository with example deployments, documentation, and resources for users to replicate and extend the application.</li>
    </ul>

    <h2>Input Data</h2>
    <p>The following input parameters are utilized in the Edge Analytics in Credit Decisioning project:</p>
    <ol>
        <li><strong>Applicant Information</strong>:
            <ul>
                <li><strong>Input Format</strong>: Form submission</li>
                <li><strong>Description</strong>: Contains personal and financial details of the loan applicant.</li>
                <li><strong>Sample Fields</strong>:
                    <ul>
                        <li><code>gender</code>: Gender of the applicant (e.g., Male, Female).</li>
                        <li><code>married</code>: Marital status (e.g., Yes, No).</li>
                        <li><code>education</code>: Education level (e.g., Graduate, Not Graduate).</li>
                        <li><code>self_employed</code>: Employment status indicating if the applicant is self-employed (e.g., Yes, No).</li>
                        <li><code>applicant_income</code>: Monthly income of the applicant.</li>
                        <li><code>coapplicant_income</code>: Monthly income of the co-applicant, if any.</li>
                        <li><code>loan_amount</code>: The amount of the loan requested.</li>
                        <li><code>loan_amount_term_months</code>: The term of the loan in months (converted to days internally).</li>
                        <li><code>credit_history</code>: Binary value indicating credit history (0 for no credit history, 1 for good credit history).</li>
                        <li><code>property_area</code>: Type of property area (e.g., Rural, Semiurban, Urban).</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ol>
      <h2>Conclusion</h2>
    <p>The credit decisions project provides a powerful tool for financial institutions or banks to streamline their loan application processes. By leveraging distributed computing and real-time analytics, this project empowers lenders to make faster, data-driven decisions that benefit both the institution and its customers.</p>
    """, unsafe_allow_html=True)

