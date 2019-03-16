import urllib
from bs4 import BeautifulSoup

url = [‘https://www.bloomberg.com/quote/CCMP:IND', ‘https://www.bloomberg.com/quote/SPX:IND']
data = []
for pg in url:
 r = urllib.request.urlopen(pg)

soup = BeautifulSoup(r, ‘html.parser’)

name = soup.find(‘h1’, attrs={‘class’: ‘name’})
 name = name.text.strip()
 print(name)

price = soup.find(‘div’, attrs={‘class’: ‘price’})
 price = price.text
 print(price)

data.append((name, price))

########## Saved to csv ##########

import csv 
from datetime import datetime

with open(‘index.csv’, ‘a’) as csv_file:
 writer = csv.writer(csv_file)
 for name, price in data:
 writer.writerow([name, price, datetime.now()])
 writer.writerow(‘’)

page = urlopen(quote_page)
