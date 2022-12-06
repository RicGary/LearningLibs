from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pt.wikipedia.org/wiki/Coleta_de_dados_web')
soup = BeautifulSoup(html.read(), 'html.parser')    # lxml tambem funciona, na verdade é até melhor

print(soup.h1)

