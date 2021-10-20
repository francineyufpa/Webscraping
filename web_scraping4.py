#from urllib.request import urlopen
import requests
# Importando a BeautifulSoup
from bs4 import BeautifulSoup

# Vamos mudar a URL
#url = 'https://www.python.org/'
#url = 'https://finance.yahoo.com/quote/VALE3.SA/history?period1=946699200&period2=1634615999&interval=1d&frequency=1d&filter=history'

url = 'https://ge.globo.com/futebol/brasileirao-serie-b/'

# lendo a URL com a urllopen
#html = urlopen(url)
html = requests.get(url).text
# Enfim mostrando o poder da bs4
#bs = BeautifulSoup(html)

# Imprimindo o título da página
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())
#for tabela in soup.findAll('div'):
#    print(tabela)
#print(len(soup.findAll('div')))
#print(soup.findAll('div', class_='classificacao__pontos-corridos'))
#print(soup.findAll('div', class_="classificacao__pontos-corridos"))
#soup.find( class_ ="classificacao__pontos-corridos")
# iterate all tags
# get all tags
tags = {tag.name for tag in soup.find_all()}
class_list = set()
for tag in tags:
  
    # find all element of tag
    for i in soup.find_all( tag ):
  
        # if tag has attribute of class
        if i.has_attr( "class" ):
  
            if len( i['class'] ) != 0:
                class_list.add(" ".join( i['class']))
  
print(class_list)