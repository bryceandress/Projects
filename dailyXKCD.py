#!/usr/bin/env python3

import requests, os, bs4, smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Defaults
url = 'http://xkcd.com'
os.makedirs('/home/bryce/Documents/xkcd', exist_ok=True)

#Download webpage
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

#Store page in soup var and look for comic and img tag

soup = bs4.BeautifulSoup(res.text)
comicElem = soup.select('#comic img')

#If there is none do nothing
if comicElem == []:
  print('Could not find comic image.')

#download img at url. save it
else:
  comicUrl = 'http:' + comicElem[0].get('src')
  print('Downloading image %s...' % (comicUrl))
  res = requests.get(comicUrl)
  res.raise_for_status()
  imageFile = open(os.path.join('/home/bryce/Documents/xkcd', os.path.basename(comicUrl)), 'wb')
  for chunk in res.iter_content(100000):
    imageFile.write(chunk)
  imageFile.close()
  print('Image saved')

#Send email with latest image
fromaddr = "Email"
toaddr = "Email"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "XKCD Comic of the Day"

body = ""
msg.attach(MIMEText(body, 'plain'))

filename = os.path.basename(comicUrl)
attachment = open("/home/bryce/Documents/xkcd/"+filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('Email', 'Password')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print('Done.')
