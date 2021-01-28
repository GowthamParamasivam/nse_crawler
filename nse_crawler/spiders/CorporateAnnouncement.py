# -*- coding: utf-8 -*-

import json
import logging
from datetime import datetime

import scrapy

from nse_crawler.items import Annoucement


class CorporateAnnouncementSpider(scrapy.Spider):
    name = 'CorporateAnnouncement'
    # start_urls = ['https://www.nseindia.com/']
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

    def start_requests(self):
        yield scrapy.Request(
            url=f'https://www.nseindia.com/api/corporate-announcements?index=equities',
            headers=self.headers,
            callback=self.parse, dont_filter=True
        )

    def parse(self, response):
        # Load the cookies
        if response.status == 401:
            logging.info("Encountered 401, Loading the cookies")
            yield scrapy.Request(
                url=f'https://www.nseindia.com/get-quotes/derivatives?symbol=BANKNIFTY',
                headers=self.headers, dont_filter=True
            )

        #parsing and processing the data
        if response.headers.get('content-type').decode("utf-8") == "application/json; charset=utf-8":
            json_response = json.loads(response.body)
            for announcement in json_response:
                annoucement_item = Annoucement()
                annoucement_item['_id'] = announcement.get('dt')
                annoucement_item['desc'] = announcement.get('desc')
                annoucement_item['dt'] = announcement.get('dt')
                annoucement_item['attchmntFile'] = announcement.get('attchmntFile')
                annoucement_item['sm_name'] = announcement.get('sm_name')
                annoucement_item['sm_isin'] = announcement.get('sm_isin')
                # annoucement_item['an_dt'] = datetime.strptime(announcement.get('an_dt'), '%d-%b-%Y %H:%M:%S')
                annoucement_item['an_dt'] = announcement.get('an_dt')
                annoucement_item['sort_date'] = announcement.get('sort_date')
                annoucement_item['seq_id'] = announcement.get('seq_id')
                annoucement_item['smIndustry'] = announcement.get('smIndustry')
                annoucement_item['orgid'] = announcement.get('orgid')
                annoucement_item['attchmntText'] = announcement.get('attchmntText')
                annoucement_item['bflag'] = announcement.get('bflag')
                annoucement_item['old_new'] = announcement.get('old_new')
                annoucement_item['csvName'] = announcement.get('csvName')
                annoucement_item['exchdisstime'] = announcement.get('exchdisstime')
                annoucement_item['difference'] = announcement.get('difference')
                yield annoucement_item

        yield scrapy.Request(
            url=f'https://www.nseindia.com/api/corporate-announcements?index=equities',
            headers=self.headers,
            callback=self.parse, dont_filter=True
        )
