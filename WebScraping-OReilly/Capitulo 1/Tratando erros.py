from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://pt.wikipedia.org/wiki/naoexiste')

except HTTPError as e:
    print(e)

except URLError as e:
    print(e)

else:
    print('Working!')
