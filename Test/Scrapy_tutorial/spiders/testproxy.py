import scrapy


class TestproxySpider(scrapy.Spider):
    name = "testproxy"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/ip"]

    def parse(self, response):
        self.log(f"Yanıt: {response.text}")
