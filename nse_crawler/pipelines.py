# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os
import pymongo
import requests
from pymongo.errors import DuplicateKeyError
from nse_crawler.items import Annoucement


class NseCrawlerPipeline:

    ANNOUNCEMENT_COLLECTION = 'annoucement'

    def open_spider(self, spider):
        logging.info("Initializing the mongo DB Client")
        self.client = pymongo.MongoClient(
            "mongodb://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("NETWORK")+":"+os.getenv("PORT")+"/?authSource=admin"
                                                                                                "&authMechanism=SCRAM"
                                                                                                "-SHA-256")
        self.db = self.client['nse_crawler']

    def process_item(self, item, spider):
        if isinstance(item, Annoucement):
            try:
                self.db[self.ANNOUNCEMENT_COLLECTION].insert(item)
                #     Sending Telegram message
                # bot_token = os.getenv("bot_token")
                # bot_chatID = os.getenv("bot_chatID")
                # constructing the message to send
                # bot_message = "Name: " + (item["sm_name"] or "Not Available") + "\n" \
                #               + "Industry: " + (item["smIndustry"] or "Not Available") + "\n" \
                #               + "Announcement Date: " + (item["an_dt"] or "Not Available") + "\n" \
                #               + "Description: " + (item["desc"] or "Not Available") + "\n" \
                #               + "Attachment Text: " + (item["attchmntText"] or "Not Available") + "\n" \
                #               + "Attachment File: " + (item["attchmntFile"] or "Not Available")
                # url_to_send_message = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                # requests.get(url_to_send_message)
            except DuplicateKeyError:
                logging.info("Duplicate Value found in the Database")
        return item

    def close_spider(self, spider):
        logging.info("Closing the mongo DB Client")
        self.client.close()
