import requests
from bs4 import BeautifulSoup
import re


html = requests.get('https://pt.wikipedia.org/wiki/Python').content
soup = BeautifulSoup(html, 'lxml')

for link in soup.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$')):
    print(link.attrs['href'])
