
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
import os
if os.path.exists("beertable.csv"):
    os.rename('beertable.csv', 'beertable_old.csv')
beerlist = pd.read_table('beerlist.txt', header=None)

beertable = pd.DataFrame(beerlist)
beertable = pd.DataFrame(beertable.values.reshape(-1, 2), columns = ['Beer', 'Brewery'])
beertable[['Brewery','Style']] = beertable['Brewery'].str.split('|',expand=True)
clean_beertable = beertable.drop_duplicates()
clean_beertable = clean_beertable.set_index('Beer')
#print(beertable)

#beertable = beertable.split('|',expand=True)
#beertable[['Brewery','Location']] = beertable['Brewery'].str.split('\(([^)]+)',expand=True)

#beertable[['Beer','ABV']] = beertable['Beer'].str.split(' * abv',expand=True)
#location = pd.find('\(([^)]+)', beertable)
#print(location)
clean_beertable.to_csv('beertable.csv')
