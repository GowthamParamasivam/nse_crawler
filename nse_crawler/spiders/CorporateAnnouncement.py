# -*- coding: utf-8 -*-
import scrapy


class CorporateAnnouncementSpider(scrapy.Spider):
    name = 'CorporateAnnouncement'
    start_urls = ['http://www.nseindia.com/']

    def parse(self, response):
        pass
