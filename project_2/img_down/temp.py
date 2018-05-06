import requests
from bs4 import BeautifulSoup
import os
import re

daily_star = requests.get('https://www.pexels.com/photo/grayscale-photo-of-trees-on-mountain-959805/')
parsed_html = BeautifulSoup(daily_star.text, "lxml")
# img_link = parsed_html.find_all('img')
images = parsed_html.find_all('img', {"src" : re.compile(r".*")})
for i in images:
    print(i, "\n")
print(len(images))
# print(img_link)
# lists = []
# def filter_image(i):
    # lists = parsed_html.find_all('img', {"data-src" : re.compile(r".*")})
    # patImgSrc = re.compile('data-srcset="(.*)"')
    # findPatImgSrc = re.findall(patImgSrc, str(i))
    # findPatImgSrc = patImgSrc.findall(imgsrc)
    # lists.append(findPatImgSrc)
    # print(lists)
# for i in img_link:
    # filter_image(i)
# img_url = map(lambda x: filter_image(x), img_link)
# print(len(lists))
#
# for i in images:
#     # print(i['data-srcset'])
#     print(i['src'])

# url = "https://www.pexels.com/photo/grayscale-photo-of-trees-on-mountain-959805/"
# response = requests.get(url)
# html = BeautifulSoup(response.text, 'lxml')
# img_link = html.find_all('img', limit=5)
# final = []
# for i in img_link:
#     if(i.get('src')):
#         final.append(i.get('src'))

# for link in final:
#     print(link, "\n")
