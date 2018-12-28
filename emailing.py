
import smtplib
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

smtpserver = 'smtp.gmail.com:587'
from_addr = 'beerscannernotif@gmail.com'
to_addr_list = ['shapiro.peter@gmail.com']
subject = 'Timmys Beer Update'
login = 'beerscannernotif'
password = 'beerscanner'

newbeer = pd.read_csv('newbeer.csv')
beerlist = pd.read_csv('beertable.csv')
oldbeer = pd.read_csv('oldbeer.csv')
beerlist = beerlist.set_index('Beer')

#body = "Beerscanners Timmy OTooles Beer List Updates" + '\n' + newbeer

header = ('Subject: %s' % subject)
body = '\n' + 'New Beer' + tabulate(newbeer, headers='keys', tablefmt='psql') + '\n' + 'Beer List' + tabulate(beerlist, headers='keys', tablefmt='psql')+ '\n' + 'Kegs Kicked' + tabulate(oldbeer, headers='keys', tablefmt='psql')

message = header + body

server = smtplib.SMTP(smtpserver)
server.starttls()
server.login(login,password)
problems = server.sendmail(from_addr, to_addr_list, message)
server.quit()
