
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import os

with open('menufile.txt') as phtml:
    contents = phtml.read()
#    print(contents)

for div in contents.select('div'):
        if div['class'] == (menu-item):
            print(div.text)

#beertext = find_all('div').text()
print(type(contents))
