"""
Encontrando imagens com bs4 e pegando seu caminho com regex.
"""
import requests
from bs4 import BeautifulSoup
import re

html = requests.get('https://nerdstore.com.br/categoria/vestuario/camisetas/').content
soup = BeautifulSoup(html, 'lxml')

pattern = r'https.+?\/uploads\/[0-9]{4}\/[0-9]{1,}\/(camiseta|vitrine).+?(jpg|jpeg|png)'

images = soup.find_all('img', {'src': re.compile(pattern)})

listed_links = [
    source.split(' ')[1] if source.split(' ')[-1] == '545w' else None for image in images
    for source in image['srcset'].split(',')
]

listed_links = list(filter(None, listed_links))

print(*listed_links, sep='\n')
