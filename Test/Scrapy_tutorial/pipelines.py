# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
"""
- Veriyi temizlemek veya doğrulamak.
- Çekilen veriyi CSV, JSON gibi dosyalara kaydetmek.
- Veriyi bir veritabanına kaydetmek.

Her bir pipeline teker teker olacak sekilde settings.py dosyasindaki ITEM_PIPELINES kismina
gore execute edilir. Bu sebepten oturu, her bir pipeline'a gelen data'nin type'ina gore
islem yapilmalidir.
Data'yi type'larina gore islem yapan pipeline'lar yazilmasi saglanir. Boylece, pipeline'a ozel items'lar ve web scraping
yontemleri yazilabilir.

--------
| Not: |
--------
"yield item" komutu calistiktan sonra settings.py kismina yazilan pipeline sirasina gore oradaki tum pipeline'lar
calistirilir.
"""
from itemadapter import ItemAdapter
import re

class TestPipeline:
    def process_item(self, item, spider):
        return item

class CleanDataPipeline:
    def process_item(self, item, spider):
        if (item.get("type") == "QuotesItem"):
            item['quote'] = item['quote'].strip()
            item['author'] = item['author'].strip()

            # Özel karakterleri kaldır
            item['quote'] = re.sub(r'[“”]', '', item['quote'])
            item['author'] = re.sub(r'[^\w\s]', '', item['author'])
        return item

class UserPipeline:
    def process_item(self, item, spider):
        if (item.get("type") == "UserItem"):
            print(f"Kullanıcı: {item['name']} işlendi.")
        return item

class PostPipeline:
    def process_item(self, item, spider):
        if (item.get("type") == "PostItem"):
            print(f"Post Title: {item['title']}.")
        return item