import requests
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Configurações do BigQuery
PROJETO = "ecommerce-data-pipeline-499213"
CREDENCIAL = "credenciais_bigquery.json"
DATASET = "bronze"
TABELA = "produtos_api"

# Autentica no BigQuery com a credencial
credenciais = service_account.Credentials.from_service_account_file(CREDENCIAL)
client = bigquery.Client(credentials=credenciais, project=PROJETO)

# Cria o dataset 'bronze' se ainda não existir
dataset_ref = f"{PROJETO}.{DATASET}"
client.create_dataset(dataset_ref, exists_ok=True)
print(f"Dataset '{DATASET}' pronto.")

# Extrai os dados da API
url = "https://fakestoreapi.com/products"
resposta = requests.get(url)
produtos = resposta.json()
df = pd.DataFrame(produtos)

# Converte a coluna 'rating' (que vem como dicionário) para texto, pra caber no BigQuery
df["rating"] = df["rating"].astype(str)

# Envia para o BigQuery (substitui a tabela a cada execução)
destino = f"{PROJETO}.{DATASET}.{TABELA}"
job = client.load_table_from_dataframe(df, destino)
job.result()  # espera terminar

print(f"{len(df)} produtos carregados em {destino}")