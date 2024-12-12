# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals
import random
import logging
from dotenv import load_dotenv
import os
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
"""
Scrapy middleware'leri, Scrapy'nin veri akışı sırasında gerçekleşen işlemleri kontrol etmeye 
ve özelleştirmeye olanak tanır. İki ana tür middleware vardır:

- Downloader Middleware: HTTP istekleri ve yanıtlarını manipüle etmek için kullanılır.
- Spider Middleware: Spider'ın işleme mantığını etkileyen middleware'dir.

Middleware, şu işlemler için kullanılır:
- Kullanıcı ajanlarını (User-Agent) değiştirme.
- Proxy kullanımı.
- Özel HTTP başlıkları ekleme.
- Dinamik bekleme süreleri (Throttle) ayarlama.
"""
# Spider'ın işleme mantığını etkileyen middleware'dir.
class TestSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

# HTTP istekleri ve yanıtlarını manipüle etmek için kullanılır.
class TestDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

"""
Proxy kullanımı, web scraping sırasında IP adresinizi değiştirerek sitelerin bot korumasını aşmanıza 
veya erişim engellerini (örneğin, bir web sitesinin aynı IP'den çok sayıda isteği engellemesi) bypass etmenize 
olanak tanır.
"""
class RandomUserAgentAndProxyMiddleware:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0"
        ]
        load_dotenv()
        self.proxies = os.getenv("PROXIES").split(", ")

        self.filtered_proxies = self.filter_working_proxies(self.proxies)

    def filter_working_proxies(self, proxies):
        # Çalışan proxy'leri test et
        working_proxies = []
        test_url = "https://httpbin.org/ip"
        for proxy in proxies:
            try:
                response = requests.get(test_url, proxies={'http': proxy, 'https': proxy}, timeout=20)
                if response.status_code == 200:
                    working_proxies.append(proxy)
            except:
                continue
        return working_proxies

    def process_request(self, request, spider):
        if not self.filtered_proxies:
            raise Exception("Çalışan proxy bulunamadı!")

        # Rastgele bir User-Agent ekle
        user_agent = random.choice(self.user_agents)

        # Rastgele bir proxy ekle
        proxy = random.choice(self.filtered_proxies)

        request.headers['User-Agent'] = user_agent
        request.meta['proxy'] = proxy

        logging.info(f"Proxy kullanılıyor: {user_agent}")
        logging.info(f"Proxy kullanılıyor: {proxy}")

