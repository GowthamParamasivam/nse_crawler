# -*- coding: utf-8 -*-
import scrapy


class CorporateannouncementSpider(scrapy.Spider):
    name = 'CorporateAnnouncement'
    allowed_domains = ['www.nseindia.com']
    start_urls = ['http://www.nseindia.com/']

    def parse(self, response):
        pass
