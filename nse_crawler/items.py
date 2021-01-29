# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NseCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Annoucement(scrapy.Item):
    _id = scrapy.Field()
    symbol = scrapy.Field()
    desc = scrapy.Field()
    dt = scrapy.Field()
    attchmntFile = scrapy.Field()
    sm_name = scrapy.Field()
    sm_isin = scrapy.Field()
    an_dt = scrapy.Field()
    sort_date = scrapy.Field()
    seq_id = scrapy.Field()
    smIndustry = scrapy.Field()
    orgid = scrapy.Field()
    attchmntText = scrapy.Field()
    bflag = scrapy.Field()
    old_new = scrapy.Field()
    csvName = scrapy.Field()
    exchdisstime = scrapy.Field()
    difference = scrapy.Field()
    isProcessed = scrapy.Field()