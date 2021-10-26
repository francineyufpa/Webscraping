from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
#import openpyxl


"""
#Informações para fingir ser um navegador

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

#juntamos tudo com a requests

html = Request(url, headers=header)
html = urlopen(html).read()
bs = BeautifulSoup(html, 'html.parser')
"""
#url = 'https://hidemy.name/en/'
url = 'https://hidemy.name/en/proxy-list/?country=BR&type=hs&anon=34' #list
html = requests.get(url).content
bs = BeautifulSoup(html, 'html.parser')
print(bs.prettify())

#tabela = bs.find('table')
#print(tabela)
#linhas = bs.find_all("tr")
#print(linhas)

## Imprime todo texto contido em cada linha ##
#for i in linhas:
#    print(i.text)

## Imprime o texto de cada uma das tags filhas ##
#for i in linhas:
#    filhas = i.findChildren("td")
#    print(filhas[0])
##   print(filhas[1])
#   print(filhas[2])

"""
codigo, descricao, periodo = [], [], []
for i in linhas:
    children = i.findChildren("td")
    codigo.append(children[0].text)
    descricao.append(children[1].text)
    periodo.append(children[2].text)


df = pd.DataFrame({'Código': codigo, 'Descrição': descricao, 'Período': periodo})
df.head(3)
#print(df['Código'])

df.to_excel('caminho_do_arquivo.xlsx')
df.to_csv('texte.csv')

#onde ‘driver_source’ é a URL para onde o Selenium está apontando naquele trecho do código.

bs = BeautifulSoup(driver_source) 

"""

