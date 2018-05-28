from urllib.request import urlopen
from bs4 import BeautifulSoup

# Global variable
url_aj = "http://www.aljazieera.com"
filepath = "html/aj.html"

class NewsScraper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self, url, wlog):
        self.__url  = url
        self.__wlog = wlog

    def rettrive_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Retrieved Successfully")