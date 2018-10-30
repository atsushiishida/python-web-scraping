import requests
from bs4 import BeautifulSoup

# URLからHTMLを取得します
url = "https://docs.pyq.jp/_static/assets/scraping/item-list.html"
response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')

# div.item-list で 囲まれた部分を抽出します
div_item_list = bs.select('div.item-list')

# div.item で囲まれた部分を抽出
for div_item in div_item_list[0].select('div.item'):
    # 商品名を抽出
    item_name_tags = div_item.select('a.item-name')
    item_name_tag  = item_name_tags[0]
    item_name      = item_name_tag.text.strip()
    # 価格を抽出
    item_price_tags = div_item.select('span.item-price')
    item_price_tag = item_price_tags[0]
    item_price = item_price_tag.text.strip()
    
    print('商品名: {} 価格: {}'.format(item_name, item_price))

