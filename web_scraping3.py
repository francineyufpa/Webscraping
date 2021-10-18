#from urllib.request import urlopen
import requests
# Importando a BeautifulSoup
from bs4 import BeautifulSoup

# Vamos mudar a URL
#url = 'https://www.python.org/'
url = https://finance.yahoo.com/quote/VALE3.SA/history?period1=946699200&period2=1634615999&interval=1d&frequency=1d&filter=history
# lendo a URL com a urllopen
#html = urlopen(url)
html = requests.get(url).content
# Enfim mostrando o poder da bs4
bs = BeautifulSoup(html)

# Imprimindo o título da página
print(bs.title.text)
print('******//\\///\\\//\\******')
h1 = bs.find_all('h1')
for tag in h1:
    print(tag)


