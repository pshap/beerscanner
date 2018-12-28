
import smtplib
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
except:
    print('Something went wrong...')

smtpserver = 'smtp.gmail.com:587'
from_addr = 'beerscannernotif@gmail.com'
to_addr_list = ['shapiro.peter@gmail.com']
cc_addr_list = ['RC@xx.co.uk']
subject = 'Timmys Beer Update'
body = 'Howdy from a python function'
login = 'beerscannernotif'
password = 'beerscanner'


header = ('Subject: %s' % subject)
message = header + '\n' + body


server = smtplib.SMTP(smtpserver)
server.starttls()
server.login(login,password)
problems = server.sendmail(from_addr, to_addr_list, message)
server.quit()
