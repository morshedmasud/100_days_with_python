import requests
import re

url = "http://books.toscrape.com/index.html"
respose = requests.get(url)
page_content = respose.text

regex = re.compile(r'<div class="side_categories">(.*?)</div>', re.M | re.DOTALL)