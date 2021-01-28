# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymongo
from pymongo.errors import DuplicateKeyError

from nse_crawler.items import Annoucement


class NseCrawlerPipeline:
    ANNOUNCEMENT_COLLECTION = 'annoucement'

    def open_spider(self, spider):
        logging.info("Initializing the mongo DB Client")
        self.client = pymongo.MongoClient(
            "mongodb://hello:hello@127.0.0.1:27017/?authSource=admin&authMechanism=SCRAM-SHA-256")
        self.db = self.client['nse_crawler']

    def process_item(self, item, spider):
        if isinstance(item, Annoucement):
            try:
                result = self.db[self.ANNOUNCEMENT_COLLECTION].insert(item)
            except DuplicateKeyError:
                logging.info("Duplicate Value found in the Database")
        return item

    def close_spider(self, spider):
        logging.info("Closing the mongo DB Client")
        self.client.close()
