# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from datetime import datetime
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class StackPipeline(object):

    # Initialize DB connection
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    # Process each item and add to DB
    def process_item(self, item, spider):
        valid = True

	# Ensure data is correct type as defined in items.py; if valid, process for DB
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # Add to DB if not present; update DB if already present (based on url)

            timestamp = str(datetime.now())

            # Check to see if present in DB; if not add; if so, update
    	    if self.collection.count({'domain': item['domain']}) == 0:
	        self.collection.insert_one({'domain': item['domain'], 
		            'processed': False,
		            'createdAt': item['time']}) 
		log.msg("URL ADDED to database!", level=log.DEBUG, spider=spider)
	    # If domain is already present, update. 
	    else:
		# TODO: Add desired logic for updating entry; here is a sample:
#	        self.collection.update_one({'url': item['url']
#		    	    }, {'$set': {
#			    'processed': False,
#			    'createdAt': timestamp}}, upsert=False)
#                log.msg("URL updated!",
#                            level=log.DEBUG, spider=spider)
		log.msg("URL SHOULD BE Updated | No update logic programmed in 'pipeline.py' file.",
			    level=log.DEBUG, spider=spider)

        return item


