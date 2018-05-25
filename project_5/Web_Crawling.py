import re
import sys
import csv
import requests
import logging
from html import unescape

def get_category_list(content):
    """get_category_list takes content of home page and return a list of categories and their urls"""

    return category_pat.findall(content)

def get_book_list(content):
    """get_book_list takes content of a book list page content and returns a list of book (name and url)"""

    content = content.replace("\n", " ")
    return book_list_pat.findall(content)

def get_product_details(content):
    """get_product_details takes content of a product page, parses the page and return detils about a product"""
    img_base = "http://books.toscrape.com"
    result = img_pat.findall(content)
    if len(result) == 0:
        logging.warn("Image url not found")
        image_url = ""
    else:
        img_url = result[0]
        img_url = img_url.replace("../../", "")
        image_url = img_base + img_url

    result = desc_pat.findall(content)
    if len(result) == 0:
        logging.warn("Description not found")
        description = ""
    else:
        description = unescape(result[0])

    result = upc_pat.findall(content)
    if len(result) == 0:
        logging.warn("UPC not found")
        upc = ""
    else:
        upc = result[0]

    result = price_pat.findall(content)
    if len(result) == 0:
        logging.warn("Price not found")
        price = ""
    else:
        price = result[0]

    result = avail_pat.findall(content)
    if len(result) == 0:
        logging.warn("Available item not found")
        availability = ""
    else:
        availability = result[0]

    return upc, price, image_url, availability, description


def get_page_content(url):
    """get_page_content takes a url and returns the content of the page"""

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e)

    if response.ok:
        return response.text
    logging.error("Can not get content from Url: " + url)
    return None

def get_next_page(url, content):
    """"Checks the content of a book list page and returns link of the next page, returns None, if there is no more next page"""

    result = next_page_pat.findall(content)
    if len(result) == 0:
        return None
    i = url.rfind("/")
    return url[0:i+1] + result[0]

def scrape_book_info(book_info, category_name):
    """gets the content of a book details page, and parses different components and stores the info"""

    book_url, book_name = book_info
    book_name = unescape(book_name)
    book_dict = {"Name": book_name, "Category": category_name}
    # sys.exit(1)

    book_url = book_url.replace("../../../", "")
    book_url = "http://books.toscrape.com/catalogue/" + book_url
    book_dict['URL'] = book_url


    print("scareping book ", book_name)
    logging.info("scraping: " + book_url)

    content = get_page_content(book_url)
    content = content.replace("\n", " ")

    upc, price, image_url, availability, description = get_product_details(content)
    book_dict["UPC"] = upc
    book_dict["Price"] = price
    book_dict["ImageURL"] = image_url
    book_dict["Availability"] = availability
    book_dict["Description"] = description

    csv_writer.writerow(book_dict)


def crawl_category(category_name, category_url):
    """crawls a particular category of book"""
    while True:
        content = get_page_content(category_url)
        book_list = get_book_list(content)
        for book in book_list:
            scrape_book_info(book, category_name)

        next_page = get_next_page(category_url, content)
        if next_page is None:
            break

        category_url = next_page

def crawl_website():
    """crawl_website() is the main function that coordinates the whole crawling task"""
    url = "http://books.toscrape.com/index.html"
    host_name = "books.toscrape.com"

    content = get_page_content(url)
    if content == "":
        logging.critical("Got empty content from " + url)
        sys.exit(1)

    category_list = get_category_list(content)
    for category in category_list:
        category_url, category_name = category

        category_url = "http://" + host_name + "/" + category_url
        print(category_url)
        crawl_category(category_name, category_url)


if __name__ == "__main__":
   # Compile different regular expression patterns
    category_pat = re.compile(r'<li>\s*<a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*?', re.M | re.DOTALL)

    next_page_pat = re.compile(r'<li class="next"><a href="(.*?)">next</a></li>')

    book_list_pat = re.compile(r'<h3><a href="(.*?)"\s*title="(.*?)">')

    img_pat = re.compile(r'<div class="item active">\s*<img src="(.*?)".*?>')

    desc_pat =  re.compile(r'<div id="product_description" class="sub-header">.*?<p>(.*?)</p>')

    upc_pat = re.compile(r'<th>UPC</th>\s*<td>(.*?)</td>')

    price_pat = re.compile(r'<th>Price \(incl. tax\)</th>\s*<td>\D+([\d.]+?)</td>')

    avail_pat = re.compile(r'<th>Availability</th>\s*<td>(.*?)</td>')


    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename='log_file/bookstore_crawler.log',level=logging.DEBUG)

    with open("csv_file/book_list.csv", "w", encoding="ISO-8859-1") as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=["Name", "Category", "UPC", "URL", "ImageURL", "Price", "Availability","Description"])
        csv_writer.writeheader()

        crawl_website()

