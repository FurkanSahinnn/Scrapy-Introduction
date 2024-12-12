from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

output_path = 'Outputs/'
# Scrapy ayarlarını al
settings = get_project_settings()

# CrawlerProcess başlat
process = CrawlerProcess(settings)

# Spider'lar ve çıktı dosyalarını tanımlayın
spiders = [
    {'name': 'api_example', 'output': output_path + 'output_api_example.json'},
    {'name': 'multipage', 'output': output_path + 'output_multipage.json'},
]

# Her bir spider için FEEDS ayarını güncelleyerek process.crawl() call et.
for spider in spiders:
    settings.set('FEEDS', {
        spider['output']: {
            'format': 'json',
            'encoding': 'utf8',
            'overwrite': True,
        }
    })
    process.crawl(spider['name'])

# Spider'ları çalıştır
process.start()

"""
Use Case:
    cd Test/Scrapy_tutorial/parallel
    python run_spiders.py
"""