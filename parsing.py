
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
import os


beerlist = pd.read_table('beerlist.txt', header=None)

beertable = pd.DataFrame(beerlist)
beertable = pd.DataFrame(beertable.values.reshape(-1, 2), columns = ['Beer', 'Brewery'])

#print(beertable)

#beertable = beertable.split('|',expand=True)
#beertable[['Brewery','Location']] = beertable['Brewery'].str.split('\(([^)]+)',expand=True)
beertable[['Brewery','Style']] = beertable['Brewery'].str.split('|',expand=True)
#beertable[['Beer','ABV']] = beertable['Beer'].str.split(' * abv',expand=True)
#location = pd.find('\(([^)]+)', beertable)
#print(location)
beertable.to_csv('beertable.csv')
