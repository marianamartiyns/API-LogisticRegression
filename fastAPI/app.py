import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Previsão de Churn", layout="wide")

# Estilo global para o Streamlit
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f8f9fa;
    }

    h1 {
        font-size: 2.2em;
        font-weight: 600;
        color: #85B8FF;
    }

    .stButton button {
        background-color: #256D85;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
    }

    .stButton button:hover {
        background-color: #1d5568;
    }

    hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
        border: none;
        height: 2px;
        background: linear-gradient(to right, #256D85, #89CFF0);
    }
    </style>
""", unsafe_allow_html=True)

# Navbar em formato de abas no topo
tabs = st.tabs(["🔎 Previsão de Churn", "📊 Dashboard"])

# ---------- ABA 1: Previsão de Churn ----------
with tabs[0]:
    st.markdown("""
        <h1 style='text-align: center;'>🔍 <span style='color:#85B8FF;'>Previsão de Churn</span></h1>
        <p style='text-align: center; color: #666;'>Preencha os dados do cliente para prever a probabilidade de desligamento.</p>
        <hr/>
    """, unsafe_allow_html=True)

    with st.form("form_churn"):
        col1, col2 = st.columns(2)

        with col1:
            Contract = st.selectbox("📄 Tipo de Contrato", [0, 1, 2], format_func=lambda x: ["Mensal", "1 ano", "2 anos"][x])
            Tech_Support = st.radio("🛠️ Suporte Técnico", [0, 1], format_func=lambda x: "Sim" if x else "Não")
            Tenure_Months = st.slider("⏳ Tempo de permanência (meses)", 0, 72)
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

        if st.form_submit_button("🔎 Prever Churn"):
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
                        prob = response.json()["churn_probability"]
                        st.success(f"✅ Probabilidade de Churn: **{prob:.2%}**")
                        st.markdown(
                            "<h3 style='color: #F15A59;'>⚠️ Alta probabilidade de desligamento.</h3>"
                            if prob > 0.5 else
                            "<h3 style='color: #256D85;'>🟢 Baixa probabilidade de desligamento.</h3>",
                            unsafe_allow_html=True
                        )
                    else:
                        st.error("Erro ao obter resposta da API.")
                except Exception as e:
                    st.error(f"Erro ao conectar com a API: {e}")

# ---------- ABA 2: Dashboard ----------
with tabs[1]:
    st.markdown("""
        <h1 style='text-align: center;'>📊 <span style='color:#85B8FF;'>Dashboard de Clientes</span></h1>
        <p style='text-align: center; color: #666;'>Visualização dos dados de clientes com relação a churn.</p>
        <hr/>
    """, unsafe_allow_html=True)

    df = pd.read_csv("data/churn_df.csv")

    df["Contract Label"] = df["Contract"].map({0: "Mensal", 1: "1 ano", 2: "2 anos"})
    df["Churn Label"] = df["Churn Value"].map({0: "Ficou", 1: "Saiu"})
    df["Gender Label"] = df["Gender"].map({0: "Masculino", 1: "Feminino"})
    df["Senior Citizen Label"] = df["Senior Citizen"].map({0: "Não Idoso", 1: "Idoso"})

    df_cancelados = df[df['Churn Label'] == "Saiu"]
    df_nao_cancelados = df[df['Churn Label'] == "Ficou"]

    # Paleta de cores
    COLOR_CHURN_FICOU = "#256D85"
    COLOR_CHURN_SAIU = "#F15A59"

    st.plotly_chart(px.histogram(
        df_cancelados, x="Tenure Months", nbins=20,
        title="Duração de Permanência - Clientes que Cancelaram",
        labels={"Tenure Months": "Meses de Permanência"},
        color_discrete_sequence=[COLOR_CHURN_SAIU]
    ).update_layout(bargap=0.1), use_container_width=True)

    st.plotly_chart(px.histogram(
        df_nao_cancelados, x="Tenure Months", nbins=20,
        title="Duração de Permanência - Clientes que Não Cancelaram",
        labels={"Tenure Months": "Meses de Permanência"},
        color_discrete_sequence=[COLOR_CHURN_FICOU]
    ).update_layout(bargap=0.1), use_container_width=True)

    df["Payment Method"] = df["Payment Method"].map({
        0: "Cheque pelo correio", 
        1: "Cheque eletrônico", 
        2: "Transferência bancária (automática)", 
        3: "Cartão de crédito (automático)"
    })

    st.plotly_chart(px.histogram(
        df, x="Payment Method", color="Churn Label", barmode="group",
        title="Churn por Método de Pagamento",
        labels={"Payment Method": "", "Churn Label": "Churn"},
        category_orders={"Payment Method": ["Cheque pelo correio", "Cheque eletrônico", 
                                            "Transferência bancária (automática)", "Cartão de crédito (automático)"]},
        color_discrete_map={"Ficou": COLOR_CHURN_FICOU, "Saiu": COLOR_CHURN_SAIU}
    ).update_layout(xaxis_tickangle=30, bargap=0.1), use_container_width=True)

    st.plotly_chart(px.histogram(
        df, x="Contract Label", color="Churn Label", barmode="group",
        title="Distribuição de Churn por Tipo de Contrato",
        labels={"Contract Label": "", "Churn Label": "Churn"},
        category_orders={"Contract Label": ["Mensal", "1 ano", "2 anos"], "Churn Label": ["Ficou", "Saiu"]},
        color_discrete_map={"Ficou": COLOR_CHURN_FICOU, "Saiu": COLOR_CHURN_SAIU}
    ), use_container_width=True)

    df_pizza_genero = df.groupby(["Gender Label", "Churn Label"]).size().reset_index(name="Contagem")

    fig_pizza_genero = px.pie(
        df_pizza_genero,
        names="Gender Label",
        values="Contagem",
        color="Gender Label",
        title="Proporção de clientes por Gênero",
        hole=0.4,
        color_discrete_map={"Masculino": "#13934A", "Feminino": "#E0086F"},
    )

    st.plotly_chart(fig_pizza_genero, use_container_width=True)

    st.plotly_chart(px.histogram(
        df, x="Gender Label", color="Churn Label", barmode="group",
        title="Distribuição de Churn por Gênero",
        labels={"Gender Label": "", "Churn Label": "Churn"},
        category_orders={"Gender Label": ["Masculino", "Feminino"], "Churn Label": ["Ficou", "Saiu"]},
        color_discrete_map={"Ficou": COLOR_CHURN_FICOU, "Saiu": COLOR_CHURN_SAIU}
    ), use_container_width=True)

    idoso_counts = df["Senior Citizen Label"].value_counts().reset_index()
    idoso_counts.columns = ["Idoso", "Contagem"]

    fig = px.pie(
        idoso_counts,
        names="Idoso",
        values="Contagem",
        title="Proporção de Clientes Idosos",
        hole=0.4,
        color="Idoso",
        color_discrete_map={"Não Idoso": "#6DA4AA", "Idoso": "#FCBF1F"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.plotly_chart(px.histogram(
        df, x="Senior Citizen Label", color="Churn Label", barmode="group",
        title="Distribuição de Churn por Idoso",
        labels={"Senior Citizen Label": " ", "Churn Label": "Churn"},
        category_orders={"Senior Citizen Label": ["Não Idoso", "Idoso"], "Churn Label": ["Ficou", "Saiu"]},
        color_discrete_map={"Ficou": COLOR_CHURN_FICOU, "Saiu": COLOR_CHURN_SAIU}
    ), use_container_width=True)
