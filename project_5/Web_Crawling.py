import re
import sys
import csv
import requests
import logging

def get_category_list(content):
    """get_category_list takes content of home page and return a list of categories and their urls"""
    pass

def get_book_list(content):
    """get_book_list takes content of a book list page content and returns a list of book (name and url)"""
    pass

def get_product_details(content):
    """get_product_details takes content of a product page, parses the page and return detils about a product"""
    pass

def get_page_content(url):
    """get_page_content takes a url and returns the content of the page"""
    pass

def get_next_page(content):
    """"Checks the content of a book list page and returns link of the next page"""
    pass

def scrape_book_info(book_info, category_name):
    """gets the content of a book details page, and parses different components and stores the info"""
    pass

def crawl_category(category_name, category_url):
    """crawls a particular catefory of book"""