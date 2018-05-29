from urllib.request import urlopen
from bs4 import BeautifulSoup

# Global variable
url_aj = "http://www.aljazeera.com"
filepath = "html/aj.html"

class NewsScraper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self, url, wlog):
        self.__url  = url
        self.__wlog = wlog

    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Retrieved Successfully")


    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as f:
                if data:
                    f.write(data)
                else:
                    f.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog(str(e))

    def read_webpage_from_html(self, filepath=filepath):
        try:
            with open(filepath) as f:
                self.__data = f.read()
        except Exception as e:
            print(e)
            self.__wlog(str(e))

    def change_url(self, url):
        self.__url = url

    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, "html.parser")

    def parse_soup_to_simple_html(self):
        news_list = self.__soup.find_all(['h1', 'h2', 'h3', 'h4'])

        htmltext = """
<html>
    <head>
        <title>Simple New link Scrapper</title>
    </head>
    <body>
        {NEWS_LINKS}
    </body>
</html>
"""

        news_links = '<ol>'
        for tag in news_list:

            if tag.parent.get('href'):
                link = self.__url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}'target='_blank'>{}</li>\n".format(link, title)
        news_links +='</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        self.write_webpage_as_html(filepath='html/simplenews.html', data=htmltext.encode())
