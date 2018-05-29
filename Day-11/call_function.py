from webscrap import wlog
from webscrap import wscrap

wlog.set_custom_log_info("html/error.log")

news_scrap = wscrap.NewsScraper(wscrap.url_aj, wlog)
news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()

news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
news_scrap.parse_soup_to_simple_html()