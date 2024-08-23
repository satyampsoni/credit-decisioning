# Credit Decisioning 
[EAnalytics Edge Ecosystem Workloads in Finance vertical](https://github.com/openSUSE/mentoring/issues/186) | [Google Summer of Code 2024, openSUSE](https://summerofcode.withgoogle.com/programs/2024/organizations/opensuse-project)


## Overview

This project is an open-source application leveraging edge analytics to asses the loan applications. The application allows users to input their details and predicts whether a loan should be approved or not, making the process accessible and user-friendly.

This project is part of **Google Summer of Code**, and special thanks to my mentors **[Bryan Gartner](https://github.com/bwgartner), [Navin Chandra](https://github.com/navin772), [Terry Smith](https://github.com/tlssuse),** and **[Ann Davis](https://github.com/andavissuse)** for their consistent support and belief in me throughout the 4 month long journey.

![image](https://github.com/user-attachments/assets/f52a5899-c704-47d7-8438-ba749838dd6e)



## Features

- **User-Friendly Interface**: A web-based interface that allows users to input loan application details easily, details below.
- **Real-Time Credit Decisions**: The application processes inputs and provides immediate decision on person's eligibility to take loan, undet the hood it uses ML model.
- **Data-Driven Insights**: The system analyzes historical data and current market conditions to inform credit decisions.
- **Open Source**: The project includes a GitHub repository with example deployments, documentation, and resources for users to replicate and extend the application.

## Input Data

Following are the input data that the application asks to make the decisions.

  - **Gender**: *Gender of the applicant (e.g., Male, Female).*
  - **Married**: *Marital status (e.g., Yes, No).*
  - **Education**: *Education level (e.g., Graduate, Not Graduate).*
  - **Self-employed**: *Employment status indicating if the applicant is self-employed (e.g., Yes, No).*
  - **Applicant_income**: *Monthly income of the applicant.*
  - **Coapplicant_income**: *Monthly income of the co-applicant, if any.*
  - **Loan_amount**: *The amount of the loan requested.*
  - **Loan_amount_term_months**: *The term of the loan in months.*
  - **Credit_history**: *Binary value indicating credit history (0 for no credit history, 1 for good credit history).*
  - **Property_area**: *Type of property area (e.g., Rural, semi-urban, Urban).*
  

### Installing in your local computer

## 1. Using Virtual Environment

1. Create a Virtual Environment, venv (you can name it anything you wish)
   ```
   python3 -m venv .venv
   ```
  
3. Activate the virtual environment.
   ```
   source .venv/bin/activate
   ```
   
5. Clone the repository
   ```
   git clone https://github.com/satyampsoni/credit-decisioning.git
   ```

6. change the directory
   ```
   cd credit-decisioning
   ```
   
7. Install all the requirements
   ```
   pip install -r requirements.txt
   ```

8. change the directory
   ```
   cd dashboard
   ```

10. Run the application
    ```
    streamlit run app.py
    ```

  You can now view your Streamlit app in your browser.
         
         Local URL: http://localhost:8501
         Network URL: http://192.168.1.8:8501
      

## 2. Using Docker 

1. Pull the Docker image
  ```
  sudo docker pull satyamosoni/credit-decisions:latest
  ```
2. Start the container
   
  ```
    Sudo docker run -d -p 8501:8501 -it credit-decisions
   ```

The project will be accessbile at
```
http://localhost:8501/
```

### 




   
   


