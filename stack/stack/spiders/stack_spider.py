import scrapy
from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem
import StringIO
import csv
import urllib
import re

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["bambenekconsulting.com"]
    start_urls = [
        "http://osint.bambenekconsulting.com/feeds/c2-dommasterlist.txt",
    ]


    # Define column structure as found in the query webpage
    column_structure = ['domain', 'reason', 'timestamp',\
                            'source']
    discard_columns = ['reason', 'source']
    comment_delimiter = "#"
    item_delimiter = ","
    skip_num_lines = 16

    def parse(self, response):
        hxs = Selector(response)
        myquery = hxs.xpath('//body').extract()[0]

	# NOTE: myquery now contains entire "raw" body web page; at beginning
	# of string is '<body><p>' and at end of string is '</p></body>'.

	f = StringIO.StringIO(myquery)
	querylist = list(csv.reader(f, delimiter=self.item_delimiter))

	items = [] 

	for i in range(self.skip_num_lines, len(querylist)):
	    if len(querylist[i]) >= 2:

        	item = StackItem()  
		item['domain'] = querylist[i][0]
		item['time'] = querylist[i][2]

        	items.append(item)  

        return items  # NOTE - return 'items' array, which will push through pipeline and contains the logic for adding to database
