
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
import os

#with open('beerlist.txt') as beerlist:
#    contents = beerlist.read()
#    print(contents)

beertable = pd.read_table('beerlist.txt', header=None)

#beertext = find_all('div').text()
print(beertable)
