from db.connection import init_connection
import pandas as pd
import streamlit as st

def execute_query(query):
    conn = init_connection()
    if conn is not None:
        try:
            df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")
        finally:
            conn.close()  # Certifique-se de fechar a conexão
    else:
        st.error("Conexão ao banco de dados não pôde ser estabelecida.")

def get_ticket_medio_por_forma_pagamento_query():
    return "SELECT formaPagto, AVG(valorTotal) AS ticket_medio \
        FROM Pedido \
        GROUP BY formaPagto;"

def get_top_selling_products_query():
    return "SELECT p.nome, SUM(c.quantidade) AS total_vendas \
        FROM produto p \
        JOIN item i ON p.idproduto = i.idproduto \
        JOIN compra c ON i.iditem = c.iditem \
        JOIN pedido pd ON c.idpedido = pd.idpedido \
        WHERE pd.statuspagto = 'Pago' \
        GROUP BY p.nome \
        ORDER BY total_vendas DESC \
        LIMIT 10;"

            