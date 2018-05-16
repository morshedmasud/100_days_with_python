# -*- coding: utf-8 -*-

import re
import requests
import sys

url = "http://dimik.pub"
response = requests.get(url)
if response.ok is False:
    sys.exit("Could not get response from server")
page_content = response.text

pat = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)

result = re.findall(pat, page_content)
print(result)
# for i in result:
#     print("Name: ", i[2])
#     print("URL: ", i[0])
#     print("Image: ", i[1])
#     print()