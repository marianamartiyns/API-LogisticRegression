# 📊 Multivariate - Logistic Regression

> Data analysis, modeling, and deployment of a logistic regression model for churn prediction, integrating a FastAPI backend and a Streamlit frontend.

## 📋 Description

This project aims to predict the likelihood of churn (service cancellation) among customers of a fictional telecommunications company using data preprocessing techniques and predictive modeling. A dataset containing information on over 7,000 customers was used, with 33 variables that include demographic characteristics, details about the services subscribed, and billing history.

## 🧩 Data Cleaning, Data Wrangling, and Model

- [x] Drop constant and non-useful columns for modeling  
- [x] Standardization of numerical features  
- [x] One-hot encoding of categorical features  
- [x] Train-test split of data  
- [x] Logistic regression model (2 versions)  
- [x] Recursive Feature Elimination (RFE)  
- [x] Results & Validation of Results (Confusion Matrix, Accuracy and Precision, Roc Curve, AUC Score) 

## 🚀 API (FastAPI)

To make predictions accessible, a FastAPI service was developed to expose the model as an endpoint.

### 🔧 How to Run the API

1. Install dependencies:
   ```sh
   pip install fastapi uvicorn scikit-learn pandas numpy
   ```
2. Start the API:
   ```sh
   uvicorn main:app --reload
   ```
3. The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
4. Interactive Swagger documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 📡 API Endpoint

- **POST /predict**
  - Input: JSON object with customer data
  - Output: JSON object with churn probability and risk category

Example request:

```json
{
    "Gender": 1,
    "Senior Citizen": 0,
    "Partner": 1,
    "Dependents": 0,
    "Tenure Months": 12,
    "Phone Service": 1,
    "Multiple Lines": 0,
    "Internet Service": 1,
    "Online Security": 0,
    "Online Backup": 1,
    "Tech Support": 1,
    "Streaming TV": 0,
    "Streaming Movies": 1,
    "Contract": 1,
    "Paperless Billing": 1
}
```

Example response:

```json
{
    "probabilidade_churn": 0.0375,
    "previsao": "Baixo risco de churn"
}
```

## 🎨 Frontend (Streamlit)

To simplify user interaction, a Streamlit web application was built, allowing intuitive input and visualization of predictions.

### 🔧 How to Run the Streamlit App

1. Install dependencies:
   ```sh
   pip install streamlit requests
   ```
2. Run the app:
   ```sh
   streamlit run app.py
   ```

### 🖥 Features

- Interactive input fields for customer attributes
- API request and response visualization
- Styled result display with probability percentage and risk category (Low and High)

- ## 🎥 Demo

![App Demo](app.gif)


> [!NOTE]  
> The code descriptions are in Portuguese 🇧🇷, although the variables and code are in English.

```py
# Author Info

# LinkedIn: https://www.linkedin.com/in/profile-mariana-martins/
# GitHub: https://github.com/marianamartiyns
# Email: marianamartiyns@gmail.com
```

<img align="right" width="40px" src="https://avatars.githubusercontent.com/u/45109972?s=200&v=4">
<img align="right" width="40px" src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
<img align="right" width ='40px' src ='https://img.icons8.com/?size=100&id=lOqoeP2Zy02f&format=png&color=000000'> </a>
<img align="right" width ='40px' src ='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg'> </a>
