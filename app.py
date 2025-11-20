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
st.subheader("Ticket Médio por Forma de Pagamento")
query1 = queries.get_ticket_medio_por_forma_pagamento_query()
df1 = queries.execute_query(query1)
if df1 is not None:
    # st.dataframe(df1)
    fig1 = px.bar(df1, x='formapagto', y='ticket_medio', title='Ticket Médio por Forma de Pagamento')
    st.plotly_chart(fig1)

st.subheader("Top 10 Produtos Vendidos")
query2 = queries.get_top_selling_products_query()
df2 = queries.execute_query(query2)
if df2 is not None:
    # st.dataframe(df2)
    fig2 = px.bar(df2, x='nome', y='total_vendas', title='Top 10 Produtos Vendidos')
    st.plotly_chart(fig2)

st.subheader("Top 3 Artistas")
query3 = queries.get_top_artists_query()
df3 = queries.execute_query(query3)
if df3 is not None:
    # st.dataframe(df3)
    fig3 = px.bar(df3, x='artista', y='total_cartas', title='Top 3 Artistas')
    st.plotly_chart(fig3)

st.subheader("Top 3 Coleções por Cartas Únicas")
query4 = queries.get_top_collections_by_unique_cards_query()
df4 = queries.execute_query(query4)
if df4 is not None:
    # st.dataframe(df4)
    fig4 = px.bar(df4, x='nome', y='total_cartas_unicas', title='Top 3 Coleções por Cartas Únicas')
    st.plotly_chart(fig4)

st.subheader("Top 10 Produtos com Maior Volatilidade de Preços")
query5 = queries.get_price_volatility_query()
df5 = queries.execute_query(query5)
if df5 is not None:
    st.dataframe(df5)
    df5['desvio_padrao'] = df5['desvio_padrao'].fillna(0)
    fig5 = px.scatter(df5, x='produto_nome', y='diferenca_preco', size='desvio_padrao',
                      title='Volatilidade de Preços dos Produtos', hover_name='produto_nome')
    st.plotly_chart(fig5)