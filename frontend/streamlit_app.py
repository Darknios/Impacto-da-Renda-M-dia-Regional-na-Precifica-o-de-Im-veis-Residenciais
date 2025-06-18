import streamlit as st
import pandas as pd
import plotly.express as px
import unicodedata
import requests


API_URL = "http://127.0.0.1:8000"


if "token" not in st.session_state:
    st.title("Login na Plataforma de Imóveis")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login = st.button("Entrar")

    if login:
        response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
        if response.status_code == 200:
            st.session_state.token = response.json()["token"]
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")
    st.stop()


st.set_page_config(page_title="Dashboard Imobiliário", layout="wide")
st.title("Análise do Impacto da Renda Média Regional no Preço de Imóveis")


def normalizar_colunas(df):
    df.columns = [
        unicodedata.normalize('NFKD', col)
        .encode('ASCII', 'ignore')
        .decode('utf-8')
        .strip()
        .lower()
        .replace(" ", "_")
        for col in df.columns
    ]
    return df


@st.cache_data
def load_data():
    df = pd.read_csv("data/dados.csv")
    df = normalizar_colunas(df)

    if "preco" in df.columns:
        df["preco"] = (
            df["preco"]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace("R$", "", regex=False)
            .str.replace(" ", "", regex=False)
            .astype(float)
        )

    if "tipo_imovel" in df.columns:
        df["tipo_imovel"] = df["tipo_imovel"].replace({"apartment": "Apartamento", "house": "Casa"})

    if "regiao" in df.columns:
        df["regiao"] = df["regiao"].replace({
            "north": "Norte", "northeast": "Nordeste", "central-west": "Centro-Oeste",
            "southeast": "Sudeste", "south": "Sul"
        })

    return df


df = load_data()


df_preview = df.head()
st.subheader("Pré-visualização dos dados")
st.dataframe(df_preview)


estados = sorted(df["estado"].dropna().unique()) if "estado" in df.columns else []
estados_opcoes = ["Todos"] + estados
estados_selecionados = st.sidebar.multiselect("Selecione o(s) Estado(s)", estados_opcoes, default=["Todos"])

tipos = sorted(df["tipo_imovel"].dropna().unique()) if "tipo_imovel" in df.columns else []
tipos_opcoes = ["Todos"] + tipos
tipos_selecionados = st.sidebar.multiselect("Selecione o(s) Tipo(s) de Imóvel", tipos_opcoes, default=["Todos"])


df_filtrado = df.copy()
if "Todos" not in estados_selecionados and "estado" in df_filtrado.columns:
    df_filtrado = df_filtrado[df_filtrado["estado"].isin(estados_selecionados)]

if "Todos" not in tipos_selecionados and "tipo_imovel" in df_filtrado.columns:
    df_filtrado = df_filtrado[df_filtrado["tipo_imovel"].isin(tipos_selecionados)]


st.subheader("Preço Médio por Região")
st.caption(f"Estados: {', '.join(estados_selecionados)} | Tipo(s): {', '.join(tipos_selecionados)}")

colunas_necessarias = {"regiao", "preco"}
if colunas_necessarias.issubset(df_filtrado.columns) and not df_filtrado.empty:
    preco_regiao = df_filtrado.groupby("regiao")["preco"].mean().reset_index()
    fig1 = px.bar(
        preco_regiao,
        x="regiao",
        y="preco",
        color="regiao",
        labels={"regiao": "Região", "preco": "Preço Médio (R$)"},
        title="Preço Médio por Região",
        text_auto=".2s"
    )
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.warning("Dados insuficientes para exibir o gráfico com os filtros selecionados.")


st.subheader("Preço médio por Estado")
if "preco" in df.columns and "estado" in df.columns:
    preco_medio_estado = df.groupby("estado")["preco"].mean().sort_values().reset_index()
    fig2 = px.bar(
        preco_medio_estado,
        x="preco",
        y="estado",
        orientation="h",
        labels={"preco": "Preço Médio (R$)", "estado": "Estado"},
        title="Preço médio dos imóveis por Estado",
        text_auto=".2s"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.error("As colunas 'preco' ou 'estado' não estão disponíveis no DataFrame.")
