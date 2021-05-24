import pandas as pd
import json
import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

client = MongoClient(host="localhost", port=27017)
db = client.db_aprendendo
brds = db['brds']

with open('arquivos/brdsPatrocinados1.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#crio arquivo Jason para ser utilizado para carga no banco de dados
with open('arquivos/MeuArquivoJson.json', 'w') as f:
    json.dump(rows, f)

#Abro o arquivo criado faço insert na linha 23
with open ('arquivos/MeuArquivoJson.json') as f:
    file_data = json.load(f)
brds.insert(file_data)

sw = db["brds"]
x = sw.find()

print (list(x))
