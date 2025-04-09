# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Carregando o modelo
with open("model/logm2.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Estrutura da entrada
class CustomerData(BaseModel):
    Contract: int
    Tech_Support: int
    Tenure_Months: int
    Online_Security: int
    Internet_Service: int
    Device_Protection: int
    Payment_Method: int
    Monthly_Charges: float
    Online_Backup: int
    Dependents: int
    Streaming_TV: int
    Streaming_Movies: int

@app.post("/predict/")
def predict(data: CustomerData):
    features = np.array([[v for v in data.dict().values()]])
    proba = model.predict_proba(features)[0][1]
    prediction = int(proba > 0.5)
    return {"churn_probability": proba, "prediction": prediction}
