import scrapy

from Scrapy_tutorial.items import QuotesItem

class MultipageSpider(scrapy.Spider):
    name = "multipage"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # yield, her veriyi Scrapy'ye teslim eder
        for quote_block in response.xpath('//div[@class="quote"]'):
            item = QuotesItem()
            item['quote'] = quote_block.xpath('span[@class="text"]/text()').get()
            item['author'] = quote_block.xpath('span/small[@class="author"]/text()').get()
            item['tags'] = quote_block.xpath('div[@class="tags"]/a[@class="tag"]/text()').getall()
            yield item # Send item to pipeline.

        # 2. "Next" butonunu bul ve bir sonraki sayfaya geç
        # <li class="next">
        #   <a href="/page/2/">Next <span aria-hidden="true">→</span></a>
        # </li>
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
