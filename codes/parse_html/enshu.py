import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

url = 'https://docs.pyq.jp/_static/assets/scraping/item-list.html'

response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text,'html.parser')

div_item = bs.select('div.item')

for item in div_item:
    release_date_text = item.select('span.item-release-date')[0].text
    release_date = dt.strptime(release_date_text,'%Y-%m-%d')
    date_from = dt(2017,5,1)
    date_to   = dt(2017,8,31)
    
    if date_from <= release_date and release_date < date_to:
        name = item.select('a.item-name')[0].text.strip()
        price = item.select('span.item-price')[0].text.strip().replace('円','').replace(',','')
        print('{} {}'.format(name,price))
