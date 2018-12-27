from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
import os


with open('beertable_old.csv', 'r') as bl1, open('beertable.csv', 'r') as bl2:
    fileone = bl1.readlines()
    filetwo = bl2.readlines()

with open('newbeer.csv', 'w') as newbeer:
    for line in filetwo:
        if line not in fileone:
            newbeer.write(line)

with open('oldbeer.csv', 'w') as oldbeer:
    for line in fileone:
        if line not in filetwo:
            oldbeer.write(line)
