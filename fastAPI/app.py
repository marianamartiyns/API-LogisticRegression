import streamlit as st
import requests

# Função para fazer a requisição para a API
def predict_churn(data):
    url = "http://127.0.0.1:8000/predict"
    response = requests.post(url, json=data)
    return response.json()

# Título da página
# st.title("🔍 Previsão de Churn - Desligamento do Cliente")
st.subheader("🔍 Previsão de Churn - Desligamento do Cliente")

# Criando campos para entrada de dados com descrições mais intuitivas
gender = st.radio("Selecione o gênero do cliente:", ["Masculino", "Feminino"])
senior_citizen = st.radio("O cliente tem 65 anos ou mais?", ["Não", "Sim"])
partner = st.radio("O cliente tem cônjuge/parceiro(a)?", ["Não", "Sim"])
dependents = st.radio("O cliente tem dependentes?", ["Não", "Sim"])
tenure_months = st.slider("Há quantos meses o cliente é assinante?", 1, 72, 12)
phone_service = st.radio("O cliente tem serviço de telefone?", ["Não", "Sim"])
multiple_lines = st.radio("O cliente tem múltiplas linhas telefônicas?", ["Não", "Sim"])
internet_service = st.radio("O cliente tem serviço de internet?", ["Não", "Sim"])
online_security = st.radio("O cliente tem segurança online?", ["Não", "Sim"])
online_backup = st.radio("O cliente tem serviço de backup online?", ["Não", "Sim"])
tech_support = st.radio("O cliente tem suporte técnico?", ["Não", "Sim"])
streaming_tv = st.radio("O cliente usa TV por streaming?", ["Não", "Sim"])
streaming_movies = st.radio("O cliente usa filmes por streaming?", ["Não", "Sim"])
contract = st.selectbox("Qual o tipo de contrato do cliente?", ["Mês a Mês", "1 Ano", "2 Anos"])
paperless_billing = st.radio("O cliente usa cobrança sem papel?", ["Não", "Sim"])

# Converter valores para o formato esperado pela API
data = {
    "Gender": 1 if gender == "Masculino" else 0,
    "Senior Citizen": 1 if senior_citizen == "Sim" else 0,
    "Partner": 1 if partner == "Sim" else 0,
    "Dependents": 1 if dependents == "Sim" else 0,
    "Tenure Months": tenure_months,
    "Phone Service": 1 if phone_service == "Sim" else 0,
    "Multiple Lines": 1 if multiple_lines == "Sim" else 0,
    "Internet Service": 1 if internet_service == "Sim" else 0,
    "Online Security": 1 if online_security == "Sim" else 0,
    "Online Backup": 1 if online_backup == "Sim" else 0,
    "Tech Support": 1 if tech_support == "Sim" else 0,
    "Streaming TV": 1 if streaming_tv == "Sim" else 0,
    "Streaming Movies": 1 if streaming_movies == "Sim" else 0,
    "Contract": 1 if contract == "1 Ano" else 2 if contract == "2 Anos" else 0,
    "Paperless Billing": 1 if paperless_billing == "Sim" else 0
}

# Quando o botão é pressionado
if st.button("📊 Prever Churn"):
    prediction = predict_churn(data)
    
    # Formatando a probabilidade como percentual
    probabilidade = prediction["probabilidade_churn"] * 100
    previsao = prediction["previsao"]
    
    st.markdown("### 🔎 Resultado da Previsão")
    
    # Criando um card visual para exibir o resultado
    st.metric(label="💡 Probabilidade de Churn", value=f"{probabilidade:.2f}%")
    
    # Exibindo a previsão de forma destacada
    if previsao == "Baixo risco de churn":
        st.success(f"✅ {previsao}")
    else:
        st.error(f"❌ {previsao}")
