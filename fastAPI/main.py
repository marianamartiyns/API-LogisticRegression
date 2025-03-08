import pickle
import pandas as pd
import statsmodels.api as sm
from fastapi import FastAPI

app = FastAPI()
with open("model/logm2.pkl", "rb") as f:
    modelo = pickle.load(f)

# features que o modelo espera
FEATURES = [
    "Gender", "Senior Citizen", "Partner", "Dependents", "Tenure Months",
    "Phone Service", "Multiple Lines", "Internet Service", "Online Security",
    "Online Backup", "Tech Support", "Streaming TV", "Streaming Movies",
    "Contract", "Paperless Billing"
]

@app.post("/predict/")
def predict(data: dict):
    try:
        # Verificando se todas as features foram enviadas
        missing_features = [f for f in FEATURES if f not in data]
        if missing_features:
            return {"error": f"Faltando as seguintes features: {missing_features}"}
    
        df = pd.DataFrame([data])
        df = df[FEATURES]
        df = sm.add_constant(df, has_constant="add")

        # Fazendo a previsão da probabilidade de churn
        churn_prob = modelo.predict(df)[0] 
        churn_prediction = "Alto risco de churn" if churn_prob > 0.5 else "Baixo risco de churn"

        return {
            "probabilidade_churn": round(churn_prob, 4),
            "previsao": churn_prediction
        }

    except Exception as e:
        return {"error": str(e)}