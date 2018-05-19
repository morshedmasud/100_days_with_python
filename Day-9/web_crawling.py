import requests
import re

# main_url = "http://books.toscrape.com/index.html"
# # Get the page content
# respose = requests.get(main_url)
# page_content = respose.text

# # Just only taking books categories from page content
# all_cat = re.compile(r'<div class="side_categories">(.*?)</div>', re.M | re.DOTALL)
# result = all_cat.findall(page_content)

# # Taking books categories link
# text2 = result[0]
# catg_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?', re.M | re.DOTALL)
# ctg = catg_pat.findall(text2)


# # Taking only mystery categories form ctg(all_book_categories)
# mystery ="http://books.toscrape.com/"+ctg[2][0]
# rsp = requests.get(mystery)
# text3 = rsp.text
# print(text3)

# # Taking all the books url from mystery cetegories
# text3 = text3.replace("\n", " ")
# book_pat = re.compile(r'<h3><a href="(.*?)"\s*title="(.*?)">')
# my_bk_link = book_pat.findall(text3)

#  # Making next page url
# next_pat = re.compile(r' <li class="next"><a href="(.*?)">next</a></li>')
# next_link = next_pat.findall(text3)
# nex = mystery.rfind('/')
# nex_l = mystery[:nex+1] + next_link[0]



book_url = "http://books.toscrape.com/catalogue/the-exiled_247/index.html"

rsp = requests.get(book_url)
page_content = rsp.text

# Finding the book image url
img_pat = re.compile(r'<div class="item active">\s*<img src=".{5}(.*?)".*?>', re.M | re.DOTALL)
img_url = img_pat.findall(page_content)
img_url = "http://books.toscrape.com" + img_url[0]

# Taking product discription
dsc_pat = re.compile(r'<div id="product_description" class="sub-header">.*?<p>(.*?)</p>', re.M | re.DOTALL)
prd_dsc = dsc_pat.findall(page_content)

# Taking product id no
pd_pat = re.compile(r'<th>UPC</th><td>(.*?)</td>')
pd_id = pd_pat.findall(page_content)

# Taking Poduct price include tax
price_pat = re.compile(r'<th>Price \(incl. tax\)</th><td>(.*?)</td>')
price = price_pat.findall(page_content)

# available item
avl_pat = re.compile(r'<th>Availability</th>\s*<td>(.*?)</td>')
in_aval = avl_pat.findall(page_content)


