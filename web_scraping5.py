from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# Vamos testar a biblioteca requests
#url = 'https://pt.proxyservers.pro/'
url = 'https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/agenda-tributaria-2020/agenda-tributaria-janeiro-2020/dia-06-01-2020'
html = requests.get(url)
bs = BeautifulSoup(html, 'html.parser')
linhas = bs.find_all('tr', {'class':'even'})
#print(html.status_code())
#print(bs.prettify())
## Imprime todo texto contido em cada linha ##
for i in linhas:
    print(i.text)
## Imprime o texto de cada uma das tags filhas ##
for i in linhas:
    filhas = i.findChildren("td")
    print(filhas[0])
    print(filhas[1])
    print(filhas[2])


#html = urlopen("https://hidemy.name/en/")
# https://hidemy.name/en/proxy-list/?country=BR&type=hs&anon=34#list
#bs = BeautifulSoup(html, 'html.parser')
#print(bs.prettify())

