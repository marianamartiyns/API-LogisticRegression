# streamlit_app/app.py
import streamlit as st
import requests

st.set_page_config(page_title="Previsão de Churn", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #4CA1FF;'>🔍 Previsão de Churn - Desligamento do Cliente</h1>
    <p style='text-align: center; color: gray;'>Preencha os dados do cliente para prever a probabilidade de churn.</p>
    <hr style='border: 1px solid #4CA1FF;'/>
""", unsafe_allow_html=True)

with st.form("form_churn"):
    col1, col2 = st.columns(2)

    with col1:
        Contract = st.selectbox("📄 Tipo de Contrato", [0, 1, 2], format_func=lambda x: ["Mensal", "1 ano", "2 anos"][x])
        Tech_Support = st.radio("🛠️ Suporte Técnico", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        Tenure_Months = st.slider("⏳ Tempo de permanência (meses)", 0, 72, step=1)
        Online_Security = st.selectbox("🔐 Segurança Online", [0, 1, 2], format_func=lambda x: ["Não", "Sim", "Sem internet"][x])
        Internet_Service = st.selectbox("🌐 Tipo de Internet", [0, 1, 2], format_func=lambda x: ["DSL", "Fibra", "Sem internet"][x])
        Monthly_Charges = st.number_input("💰 Valor Mensal (R$)", 0.0, 200.0, step=1.0)

    with col2:
        Device_Protection = st.radio("🛡️ Proteção de Dispositivo", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        Payment_Method = st.selectbox("💳 Método de Pagamento", [0, 1, 2, 3],
                                      format_func=lambda x: ["Cartão crédito", "Fatura", "Cartão débito", "Transferência"][x])
        Online_Backup = st.selectbox("☁️ Backup Online", [0, 1, 2], format_func=lambda x: ["Não", "Sim", "Sem internet"][x])
        Dependents = st.radio("👨‍👩‍👧 Dependentes", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        Streaming_TV = st.radio("📺 Streaming de TV", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        Streaming_Movies = st.radio("🎬 Streaming de Filmes", [0, 1], format_func=lambda x: "Sim" if x else "Não")

    submitted = st.form_submit_button("🔎 Prever Churn")

    if submitted:
        input_data = {
            "Contract": Contract,
            "Tech_Support": Tech_Support,
            "Tenure_Months": Tenure_Months,
            "Online_Security": Online_Security,
            "Internet_Service": Internet_Service,
            "Device_Protection": Device_Protection,
            "Payment_Method": Payment_Method,
            "Monthly_Charges": Monthly_Charges,
            "Online_Backup": Online_Backup,
            "Dependents": Dependents,
            "Streaming_TV": Streaming_TV,
            "Streaming_Movies": Streaming_Movies
        }

        with st.spinner("⏳ Enviando dados para o modelo..."):
            try:
                response = requests.post("http://localhost:8000/predict/", json=input_data)
                if response.status_code == 200:
                    result = response.json()
                    prob = result["churn_probability"]
                    st.success(f"✅ Probabilidade de Churn: **{prob:.2%}**")
                    if prob > 0.5:
                        st.markdown("<h3 style='color: red;'>⚠️ Alta probabilidade de desligamento.</h3>", unsafe_allow_html=True)
                    else:
                        st.markdown("<h3 style='color: #068062;'>🟢 Baixa probabilidade de desligamento.</h3>", unsafe_allow_html=True)
                else:
                    st.error("Erro ao obter resposta da API.")
            except Exception as e:
                st.error(f"Erro ao conectar com a API: {e}")
