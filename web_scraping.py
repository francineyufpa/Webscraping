import pandas as pd
#import pandas_datareader as pdr
import datetime
import numpy as np

#from pandas_datareader import data as web


#dados = web.DataReader('VALE3.SA', data_source='yahoo', start='2000-1-1')
#dados

#https://finance.yahoo.com/quote/VALE3.SA/history?period1=946699200&period2=1634615999&interval=1d&frequency=1d&filter=history

#url = 'https://finance.yahoo.com'
#url = 'http://pythonscraping.com/pages/page1.html'
#url = 'www.globo.com'
# Importando as libs
from urllib.request import urlopen

# Definimos a url alvo. obs: esta url vem de um livro sobre o assunto do tópico
url = 'http://pythonscraping.com'

# Aplicamos uma requisição para pegar o HTML
html = urlopen(url)

# Verificação do conteúdo
html.read()