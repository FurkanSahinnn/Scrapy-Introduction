import requests
import os
from dotenv import load_dotenv

load_dotenv()

proxies = os.getenv("PROXIES").split(", ")
# Test edilecek URL
url = 'https://httpbin.org/ip'  # Bu site, gelen isteğin IP adresini döndürür.

# Proxy'leri tek tek test et
for proxy in proxies:
    try:
        print(f"Proxy test ediliyor: {proxy}")
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=10)
        print(f"Proxy başarılı: {response.json()}") # {response.json()}
    except Exception as e:
        print(f"Proxy başarısız: {proxy} | Hata: {e}")

"""
Use Case:
    cd Test/Testing
    python test_proxy.py
"""

