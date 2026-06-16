import requests
import pandas as pd

# URL da Fake Store API - produtos de um e-commerce fictício
url = "https://fakestoreapi.com/products"

# Faz a chamada à API
resposta = requests.get(url)
produtos = resposta.json()

# Coloca os dados em uma tabela (DataFrame) pra visualizar melhor
df = pd.DataFrame(produtos)

# Mostra quantos produtos vieram e as primeiras linhas
print(f"Total de produtos recebidos: {len(df)}")
print(df[["id", "title", "price", "category"]].head())