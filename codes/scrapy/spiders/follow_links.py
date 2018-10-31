import scrapy


class FollowLinksSpider(scrapy.Spider):
    name = 'follow_links'
    allowed_domains = ['docs.pyq.jp']
    start_urls = [
        'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
    ]

    def parse(self, response):
        div_item_list = response.css('div,item-list')[0]
        for div_item in div_item_list.css('div.item'):
            # 商品URLの取得
            item_url = div_item.css('a.item-name::attr(href)').extract_first()

            # 商品URLを個別にスクレイピング
            yield scrapy.Request(item_url, callback=self.parse_item_page)

    def parse_item_page(self, response):
        # 商品ページのHTML解析

        # 商品URLの取得
        item_url = response.url
        # 商品名の取得
        item_name = response.css('h1.item-name::text').extract_first()
        item_name = item_name.strip()

        # メーカーの取得
        item_maker = response.css('span.item-maker::text').extract_first()
        item_maker = item_maker.strip()
        # 価格の取得
        item_price = response.css('span.item-price::text').extract_first()
        item_price = item_price.strip()
        # 在庫の取得
        item_stock = response.css('span.item-stock::text').extract_first()
        item_stock = item_stock.strip()
        # 発売日の取得
        item_release_date = response.css('span.item-release-date::text').extract_first()
        item_release_date = item_release_date.strip()
        # 解析した内容を辞書にする
        item_info = {
            'name': item_name,
            'maker': item_maker,
            'price': item_price,
            'stock': item_stock,
            'release_date': item_release_date,
            'url': item_url,
        }
        
        return item_info

