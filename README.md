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
   python3 -m venv .venv //python3.10 or above 
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
  sudo docker pull satyampsoni/credit-decisions:latest
  ```
2. Start the container
   
  ```
    sudo docker run -d -p 8501:8501 -it credit-decisions
   ```

The project will be accessbile at
```
http://localhost:8501/
```

## Deploy on Kubernetes (k3s) Managed by [Rancher by SUSE](https://www.rancher.com/products/rancher/?_gl=1*1v5bynd*_gcl_au*Mzg0Nzk3MTMxLjE3MjQ1MDE1MDI.*_ga*MTgwMzQ3Njk1NC4xNzIzNDg2Njkx*_ga_JEVBS2XFKK*MTcyNDQ5NDQ3My4xMC4xLjE3MjQ1MDE1MTIuNTAuMC4w)

1. Prepare the linux host machine 
   - Processor: 2 vCPUs
   - Memory: 4 GB RAM
   - Storage: 10 GB (available)
   - operating system: Linux (SLES 15 SP4 or later is recommended).
   - Docker installed

2. Start the server
   ```
   $ sudo docker run --privileged -d --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher
   ```

3. To view the web UI, open your browser and navigate to the following address
   ```
   http://<your-host-ip>:80
   ```
4. Copy the following command and paste it into your terminal, replacing `container-id` with the actual ID of your Rancher server container:

   ```
   docker logs container-id 2>&1 | grep "Bootstrap Password:"
   ```
5. You will get a bootstrap password. Use this to log into the Rancher Dashboard by copying and pasting it

 6. The Rancher dashboard will load; click on the "Create" button to create a cluster.

 7. Enter the cluster details and in the base (kuberentes version) select the k3s one.

 8. upon clicking create button, you'll be directed to the Registration tab in step 2. Click on "_Insecure_" to bypass TLS verification, and then copy the curl command to and paste it to  register the Linux machine.

9.  Go to manage cluster in the dashboard, select _credit-decisons_ cluster and download the kubeconfig file.

10. To set the kubeconfig file as an environment variable in your terminal for deployment, you can use the export command
   ```
   export KUBECONFIG=/path/to/your/kubeconfig
   ```
11. clone the repository now 

   ```
   git clone https://github.com/satyampsoni/credit-decisioning.git
   ```

12. Navigate to the base directory, where [kustomization file](https://github.com/satyampsoni/credit-decisioning/blob/master/k8s/base/kustomization.yaml) is present

   ```
   cd credit-decisioning/k8s/base
   ```

13. Deploy the applcation

   ```
   kubectl apply -k .
   ```
_Note: The -k option tells kubectl to process the kustomization file in the directory._

14. You can now access the application at the service-ip:<port>











   
   


