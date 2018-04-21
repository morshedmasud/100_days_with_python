import requests
from bs4 import BeautifulSoup
import re
import sys

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
            question_mark = item.find("?")
            temp = requests.get(item[:question_mark])
            # every time create a new file and download the imaged
            with open("Day-3/img_down/img"+str(count) + ".jpeg", "wb") as f:
                f.write(temp.content)
        count += 1

url = "https://www.pexels.com/photo/grayscale-photo-of-trees-on-mountain-959805/"
img_downloader(url)