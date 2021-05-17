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
import re

#acesso a pagina de brds da B3
url = 'http://bvmf.bmfbovespa.com.br/cias-listadas/Mercado-Internacional/Mercado-Internacional.aspx'

html_text = requests.get(url).text

response = requests.get(url)
soup = BeautifulSoup(html_text,'html.parser')
df = pd.read_html(response.content,attrs = {'id': 'tblBdrs'})[0]

#crio o arquivo html apenas com o id que preciso
with open('arquivos/brdsPatrocinados.html','w') as f:
 f.write(str(soup.find(id='tblBdrs')))

#para criar o csv
path  = 'arquivos/brdsPatrocinados.html'

#aumentar quantidade de colunas 
list_header = [1]
soup = BeautifulSoup(open(path),'html.parser')

header = soup.find_all("table")[0].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
data = []
for element in HTML_data[1:]:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text()) 
            td_check = sub_element.find('a')
            link = sub_element.a['href']
            sub_data.append(link)
        except:
            continue
        data.append(sub_data)

dataFrame = pd.DataFrame(data=data, columns=list_header)

dataFrame = dataFrame.rename(columns = {'Clique sobre o BDR desejado':'BrdName'})
dataFrame = dataFrame.rename(columns = {'Segmento':'CodigoCvm'})

dataFrame[1] = dataFrame[1].str.strip()
dataFrame["CodigoCvm"] = dataFrame["CodigoCvm"].str.strip()

dataFrame.to_csv('arquivos/brdsPatrocinados.csv', index = False)

df = pd.read_csv('arquivos/brdsPatrocinados.csv')
df.loc[df.duplicated(), :]
df.pop("BDR's Relevantes")

df.drop_duplicates(subset ="BrdName", keep = 'first', inplace = True)
df.to_csv('arquivos/brdsPatrocinados1.csv', index=False)

#Excluo o arquivo com dados duplicados
os.remove('arquivos/brdsPatrocinados.csv')