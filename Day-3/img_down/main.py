import requests
from bs4 import BeautifulSoup
import re

def img_downloader(url):
    response = requests.get(url)
    parsed_html = BeautifulSoup(response.text, "lxml")
    img_link = parsed_html.find_all('img', {"src" : re.compile(r".*")})
    src_link = []
    final_link = []
    count = 1
    for link in img_link:
        src_link.append(link.get('src'))

    for item in src_link:
        if re.match("https:", item):
            temp = requests.get(item)
            with open("Day-3/img_down/img"+str(count) + ".jpeg", "wb") as f:
                f.write(temp.content)
        count += 1
    return final_link

url = "https://www.pexels.com/photo/grayscale-photo-of-trees-on-mountain-959805/"
img_downloader(url)