import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()

def conecta():
    try:
        conn = psycopg2.connect(
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "acoes")
        )
        print("Conectado ao PostgreSQL com sucesso!")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

def encerra_conexao(conn):
    if conn:
        conn.close()
        print("Conexão encerrada com o banco de dados!")
