import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from google.cloud import bigquery
from google.oauth2 import service_account

# Configurações
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
PROJETO = "ecommerce-data-pipeline-499213"
CREDENCIAL = "credenciais_bigquery.json"
DATASET = "bronze"

# Conecta no Neon e no BigQuery
engine = create_engine(DATABASE_URL)
credenciais = service_account.Credentials.from_service_account_file(CREDENCIAL)
client = bigquery.Client(credentials=credenciais, project=PROJETO)
client.create_dataset(f"{PROJETO}.{DATASET}", exists_ok=True)

# Lê as duas tabelas do Neon e leva cada uma pra bronze
for tabela in ["clientes", "pedidos"]:
    df = pd.read_sql(f"SELECT * FROM {tabela}", engine)
    destino = f"{PROJETO}.{DATASET}.{tabela}"
    job = client.load_table_from_dataframe(df, destino)
    job.result()
    print(f"{len(df)} registros carregados em {destino}")