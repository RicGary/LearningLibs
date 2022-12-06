import requests
from bs4 import BeautifulSoup

html = requests.get('https://pt.wikipedia.org/wiki/Python')
soup = BeautifulSoup(html, 'lxml')

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])