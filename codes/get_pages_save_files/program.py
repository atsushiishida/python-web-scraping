import requests
import time

url_1 = 'https://docs.pyq.jp/_static/assets/scraping/ensyu1.html'
url_2 = 'https://docs.pyq.jp/_static/assets/scraping/ensyu1.csv'

response = requests.get(url_1)
response.encoding = response.apparent_encoding

with open('ensyu1.html','w', encoding='utf-8') as f:
    f.write(response.text)
    
time.sleep(1)
    
response = requests.get(url_2)
response.encoding = response.apparent_encoding

with open('ensyu1.csv','w', encoding='utf-8') as f:
    f.write(response.text)
    
print('保存完了')
