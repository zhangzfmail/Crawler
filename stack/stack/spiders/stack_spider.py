from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["bambenekconsulting.com"]
    start_urls = [
        "http://osint.bambenekconsulting.com/feeds/c2-dommasterlist.txt",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//pre')
