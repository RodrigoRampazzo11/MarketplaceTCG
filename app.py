import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

# Configuração da página
st.set_page_config(
    page_title="Marketplace TCG - Analytics Dashboard",
    page_icon="coloque_um_icone",
    layout="wide"
)

# Título da aplicação
st.title("Marketplace TCG Analytics Dashboard")
st.markdown("Análise interativa de dados Marketplace TCG")
