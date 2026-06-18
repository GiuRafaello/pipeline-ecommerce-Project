import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
from google.cloud import bigquery
from google.oauth2 import service_account

# Configurações
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
PROJETO = "ecommerce-data-pipeline-499213"
CREDENCIAL = "credenciais_bigquery.json"
DATASET = "bronze"
TABELA = "avaliacoes"

# Conecta no Mongo e lê as avaliações
mongo = MongoClient(MONGO_URL)
colecao = mongo["ecommerce"]["avaliacoes"]
dados = list(colecao.find())

# Transforma em tabela e remove o campo interno _id do Mongo
df = pd.DataFrame(dados)
df = df.drop(columns=["_id"])

# Conecta no BigQuery e envia
credenciais = service_account.Credentials.from_service_account_file(CREDENCIAL)
client = bigquery.Client(credentials=credenciais, project=PROJETO)
destino = f"{PROJETO}.{DATASET}.{TABELA}"
job = client.load_table_from_dataframe(df, destino)
job.result()

print(f"{len(df)} avaliações carregadas em {destino}")