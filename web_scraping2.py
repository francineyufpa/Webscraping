# Importando a Requests
import requests

# Vamos testar a biblioteca requests
url = 'http://pythonscraping.com/pages/page1.html'
html = requests.get(url)

# Diferente da urllib, usamos text para apresentar o conteudo que o get nos trouxe
print(html.text)


