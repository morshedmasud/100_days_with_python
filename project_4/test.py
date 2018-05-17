
# import re
# import requests
# import sys

# url = "http://dimik.pub/wp-content/uploads/2018/01/gonit-korbo-joy-cover-350x450.png"

# r = requests.get(url)
# with open("nfdfdf.png", 'wb') as f:
#     f.write(r.content)

# url = "http://dimik.pub"
# response = requests.get(url)
# if response.ok is False:
#     sys.exit("Could not get response from server")
# page_content = response.text

# pat = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)

# result = re.findall(pat, page_content)
# print(result)
# for i in result:
#     print("Name: ", i[2])
#     print("URL: ", i[0])
#     print("Image: ", i[1])
#     print()

import re
import sys
import requests
from bs4 import BeautifulSoup

def img_downloader(url):
    # using request get() for connect the url
    response = requests.get(url)
    # If failed to connect url then show this message
    if response.ok is False:
        sys.exit("Error downloadin the images")
    # using Beautifulsoup for convert html to text format
    parsed_html = BeautifulSoup(response.text, "lxml")
    # using find_all() for find link where img tag with src
    img_link = parsed_html.find_all('img', {"src" : re.compile(r".*")})
    src_link = []
    count = 1
    # make a loop in img_link for find only img src_link
    for link in img_link:
        src_link.append(link.get('src'))

    # make loop in src_link for find only link where it's start with https:
    for item in src_link:
        if re.match("https:", item):
            # question_mark = item.find("?")
            # temp = requests.get(item[:question_mark])
            temp = requests.get(item)
            # every time create a new file and download the imaged
            with open("im5g"+str(count) + ".jpg", "wb") as f:
                f.write(temp.content)
        count += 1

url = "http://dimik.pub"
img_downloader(url)