import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega a senha do banco do arquivo .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Conecta ao Neon
engine = create_engine(DATABASE_URL)

# Lê o CSV de pedidos
caminho = r"C:\Users\giu_r\Downloads\pedidos.csv.csv"
df = pd.read_csv(caminho)

# Remove espaços em branco dos nomes das colunas
df.columns = df.columns.str.strip()

# Converte a coluna de data do formato dia/mês/ano
df["data_pedido"] = pd.to_datetime(df["data_pedido"], format="%d/%m/%Y").dt.date

# Envia os dados para a tabela 'pedidos' no Neon
df.to_sql("pedidos", engine, if_exists="append", index=False)

print(f"{len(df)} pedidos importados com sucesso!")