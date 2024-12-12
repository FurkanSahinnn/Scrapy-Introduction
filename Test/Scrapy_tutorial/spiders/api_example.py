from typing import Iterable

import scrapy
import json
from Scrapy_tutorial.items import UserItem, PostItem
from scrapy import Request

class ApiExampleSpider(scrapy.Spider):
    name = "api_example"
    allowed_domains = ["jsonplaceholder.typicode.com"]
    start_urls = [
        "https://jsonplaceholder.typicode.com/users",
        #"https://jsonplaceholder.typicode.com/posts"
    ]
    """
    def start_requests(self):
        urls = [
            ("https://jsonplaceholder.typicode.com/users", "users.json"),
            ("https://jsonplaceholder.typicode.com/posts", "posts.json")
        ]
        for url, fileName in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={"filename": fileName})
    """
    def parse(self, response):
        if ("users" in response.url):
            yield from self.parse_users(response) # parse_users method'unun yield'ini alir.
        elif ("users" in response.url):
            yield from self.parse_posts(response)

    def parse_posts(self, response):
        posts = json.loads(response.text)
        for post in posts:
            item = PostItem()
            item["user_id"] = post["userId"]
            item["id"] = post["id"]
            item["title"] = post["title"]
            item["body"] = post["body"]
            yield item

    def parse_users(self, response):
        users = json.loads(response.text)
        for user in users:
            item = UserItem()
            item['id'] = user['id']
            item['name'] = user['name']
            item['username'] = user['username']
            item['email'] = user['email']
            item['phone'] = user['phone']
            item['website'] = user['website']

            """
            "address" : { 
                "street": ...,
                "suite": ...,
                ...
                ...
            }
            """

            address = user['address']
            item['address_street'] = address['street']
            item['address_suite'] = address['suite']
            item['address_city'] = address['city']
            item['address_zipcode'] = address['zipcode']
            item['address_geo_lat'] = address['geo']['lat']
            item['address_geo_lng'] = address['geo']['lng']

            # Company bilgisi
            company = user['company']
            item['company_name'] = company['name']
            item['company_catchphrase'] = company['catchPhrase']
            item['company_bs'] = company['bs']

            yield item

