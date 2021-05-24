import pandas as pd
import json
import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

client = MongoClient(host="localhost", port=27017)
db = client.db_aprendendo
brds = db['brds']
      

with open ('arquivos/brdsPatrocinados.json') as f:
    file_data = json.load(f)
brds.insert(file_data)

sw = db["brds"]
x = sw.find()

print (list(x))
