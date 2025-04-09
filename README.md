# 📊 Customer Churn Prediction - Multivariate Logistic Regression

> End-to-end machine learning project with logistic regression to predict customer churn, using FastAPI for the backend and Streamlit for a modern, interactive frontend.

### 📋 Project Overview

This project predicts the likelihood of **customer churn** (service cancellation) for a telecommunications company. Using customer service, billing, and demographic data, it estimates whether a customer is at high risk of leaving.

- Cleaned dataset with over 7,000 customers
- More than 30 input features
- Integrated machine learning + API + frontend interface

### 🧪 Model Pipeline

- [x] Feature selection and cleaning
- [x] One-hot encoding for categorical variables
- [x] Standardization of numerical features
- [x] Recursive Feature Elimination (RFE)
- [x] Logistic Regression training
- [x] Model evaluation (Confusion Matrix, Accuracy, Precision, AUC)
- [x] Model serialization with `pickle`

### 🚀 Backend - FastAPI

The model is served using a FastAPI backend for real-time predictions.

#### Running the API

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn scikit-learn pandas numpy
   ```

2. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the Swagger docs at:
   - [http://localhost:8000/docs](http://localhost:8000/docs)

#### API Endpoint

- **POST** `/predict`
  - **Input**: JSON with customer attributes
  - **Output**: Churn probability and prediction (0 = no churn, 1 = churn)

#### Example Request:

```json
{
  "Contract": 0,
  "Tech_Support": 1,
  "Tenure_Months": 10,
  "Online_Security": 2,
  "Internet_Service": 1,
  "Device_Protection": 0,
  "Payment_Method": 2,
  "Monthly_Charges": 85.90,
  "Online_Backup": 0,
  "Dependents": 0,
  "Streaming_TV": 1,
  "Streaming_Movies": 1
}
```

#### Example Response:

```json
{
  "churn_probability": 0.742,
  "prediction": 1
}
```

### 🎨 Frontend - Streamlit

An interactive frontend built with Streamlit allows users to input customer data and view real-time predictions in an intuitive and styled interface.

#### Running the App

1. Install dependencies:
   ```bash
   pip install streamlit requests
   ```

2. Launch the app:
   ```bash
   streamlit run app.py
   ```

#### App Features

- User-friendly input forms with radio buttons, sliders, and dropdowns
- Clean two-column layout for better organization
- Real-time API communication
- Styled result output with probability, colors, and risk icons (🟢 / 🔴)
- Error handling and loading animations

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
