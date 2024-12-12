# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuotesItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class UserItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    username = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()

    # Address bilgisi
    address_street = scrapy.Field()
    address_suite = scrapy.Field()
    address_city = scrapy.Field()
    address_zipcode = scrapy.Field()
    address_geo_lat = scrapy.Field()
    address_geo_lng = scrapy.Field()

    # Company bilgisi
    company_name = scrapy.Field()
    company_catchphrase = scrapy.Field()
    company_bs = scrapy.Field()

class PostItem(scrapy.Item):
    user_id = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()