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

def get_data_query():
    return "SELECT * FROM usuario;"