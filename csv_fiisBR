__author__ = "Paulo Eduardo Heitor Silva"
__copyright__ = "Copyright 2021"
__credits__ = ["Paulo Eduardo Heitor Silva"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "PEHS"
__email__ = "paulos008@gmail.com"
__status__ = "Production"

import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import requests


#acesso a pagina de fiss
url = 'https://www.fundsexplorer.com.br/ranking'

response = requests.get(url)

#salvo o arquivo da internet 
with open('arquivos/fiis_atualizado.html','w') as f:
 f.write(response.text)

#abro o arquivo para leitura
with open('arquivos/fiis_atualizado.html','r') as f:
#instancio beautifulSoup para usar os dados
 soup = BeautifulSoup(f,'lxml')

#pego a parte que preciso e que vou exibir na tela e no arquivo
tag = soup.find(id='table-ranking')
print (tag)

#agora eu consegui!
with open('arquivos/fiis_atualizado.html','w') as f:
 f.write(str(soup.find(id='table-ranking')))


#abro o arquivo para leitura
path  = 'arquivos/fiis_atualizado.html'
data = []

list_header = []
soup = BeautifulSoup(open(path),'html.parser')

header = soup.find_all("table")[0].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
        data.append(sub_data)

dataFrame = pd.DataFrame(data=data, columns=list_header)

dataFrame.sort_values("Códigodo fundo", inplace = True)

dataFrame.to_csv('arquivos/MinhaTabelaDeFiss.csv', index = False)


df = pd.read_csv('arquivos/MinhaTabelaDeFiss.csv')


df.loc[df.duplicated(), :]
df.drop_duplicates(subset ="Preço Atual", keep = 'first', inplace = True)
df.to_csv('arquivos/MinhaTabelaDeFiss1.csv')

#Excluo o arquivo com dados duplicados
os.remove('arquivos/MinhaTabelaDeFiss.csv')
