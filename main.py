import pickle
import pandas as pd
import statsmodels.api as sm
from fastapi import FastAPI

# Criar a aplicação FastAPI
app = FastAPI()

# Carregar o modelo salvo
with open("logm2.pkl", "rb") as f:
    modelo = pickle.load(f)

# Definir as features que o modelo espera
FEATURES = [
    "Gender", "Senior Citizen", "Partner", "Dependents", "Tenure Months",
    "Phone Service", "Multiple Lines", "Internet Service", "Online Security",
    "Online Backup", "Tech Support", "Streaming TV", "Streaming Movies",
    "Contract", "Paperless Billing"
]

@app.post("/predict/")
def predict(data: dict):
    try:
        # Verificar se todas as features foram enviadas
        missing_features = [f for f in FEATURES if f not in data]
        if missing_features:
            return {"error": f"Faltando as seguintes features: {missing_features}"}

        # Converter os dados para DataFrame
        df = pd.DataFrame([data])

        # Garantir que as colunas estão na ordem correta
        df = df[FEATURES]

        # Adicionar a constante para a regressão logística
        df = sm.add_constant(df, has_constant="add")

        # Fazer a previsão da probabilidade de churn
        churn_prob = modelo.predict(df)[0]  # Pegamos o primeiro valor

        # Classificar como "churn" ou "não churn"
        churn_prediction = "Alto risco de churn" if churn_prob > 0.5 else "Baixo risco de churn"

        # Retornar os resultados
        return {
            "probabilidade_churn": round(churn_prob, 4),
            "previsao": churn_prediction
        }

    except Exception as e:
        return {"error": str(e)}