import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os
import db.queries as queries

# Configuração da página
st.set_page_config(
    page_title="Marketplace TCG - Analytics Dashboard",
    page_icon="coloque_um_icone",
    layout="wide"
)

# Título da aplicação
st.title("Marketplace TCG Analytics Dashboard")
st.markdown("Análise interativa de dados Marketplace TCG")

# Carregar dados
query1 = queries.get_ticket_medio_por_forma_pagamento_query()
df = queries.execute_query(query1)
if df is not None:
    st.dataframe(df)

query2 = queries.get_top_selling_products_query()
df = queries.execute_query(query2)
if df is not None:
    st.dataframe(df)

query3 = queries.get_top_artists_query()
df = queries.execute_query(query3)
if df is not None:
    st.dataframe(df)

query4 = queries.get_top_collections_by_unique_cards_query()
df = queries.execute_query(query4)
if df is not None:
    st.dataframe(df)

query5 = queries.get_price_volatility_query()
df = queries.execute_query(query5)
if df is not None:
    st.dataframe(df)