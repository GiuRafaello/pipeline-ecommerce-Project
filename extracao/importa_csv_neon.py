import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega a senha do banco do arquivo .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Conecta ao Neon
engine = create_engine(DATABASE_URL)

# Lê o CSV de clientes
caminho = r"C:\Users\giu_r\Downloads\clientes.csv.csv"
df = pd.read_csv(caminho)

# Remove espaços em branco dos nomes das colunas
df.columns = df.columns.str.strip()

# Converte a coluna de data do formato dia/mês/ano
df["data_cadastro"] = pd.to_datetime(df["data_cadastro"], format="%d/%m/%Y").dt.date

# Envia os dados para a tabela 'clientes' no Neon
df.to_sql("clientes", engine, if_exists="append", index=False)

print(f"{len(df)} clientes importados com sucesso!")