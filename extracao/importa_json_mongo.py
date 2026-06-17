import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carrega a connection string do arquivo .env
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

# Conecta ao MongoDB Atlas
cliente = MongoClient(MONGO_URL)

# Cria/usa o banco 'ecommerce' e a coleção 'avaliacoes'
db = cliente["ecommerce"]
colecao = db["avaliacoes"]

# Lê o arquivo JSON de avaliações
caminho = r"C:\Users\giu_r\Downloads\avaliacoes.json.json"
with open(caminho, "r", encoding="utf-8") as f:
    avaliacoes = json.load(f)

# Insere todos os documentos na coleção
colecao.insert_many(avaliacoes)

print(f"{len(avaliacoes)} avaliações importadas com sucesso!")