from bs4 import BeautifulSoup
import requests
import re


pages = set()
def getLinks(pageUrl):
    html = requests.get(f'https://pt.wikipedia.org{pageUrl}').content
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.find_all('a', href=re.compile(r'^(/wiki/)')):
        if ('href' in link.attrs) and (link.attrs['href'] not in pages):
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)


getLinks('')