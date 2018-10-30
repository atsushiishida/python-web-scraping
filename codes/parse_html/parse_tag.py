import requests
from bs4 import BeautifulSoup

# URLからHTMLを取得します
url = "https://docs.pyq.jp/_static/assets/scraping/parse1.html"
response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')

# ulタグで囲まれた部分を抽出します
ul_tag = bs.find('ul')

# ulタグの中のaタグを抽出します
for a_tag in ul_tag.find_all('a'):

    # aタグのテキストを取得
    text = a_tag.text
    # aタグのhref属性を取得
    link_url = a_tag['href']
    # 表示します
    print('{}: {}'.format(text, link_url))

