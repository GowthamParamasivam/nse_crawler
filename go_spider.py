import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from nse_crawler.spiders.CorporateAnnouncement import CorporateAnnouncementSpider

# checking the environment Variable
if os.getenv("PORT") is None:
    raise Exception("Port not found")
if os.getenv("USERNAME") is None:
    raise Exception("Username not found in")
if os.getenv("PASSWORD") is None:
    raise Exception("Password not found")
if os.getenv("NETWORK") is None:
    raise Exception("Network not found")


process = CrawlerProcess(get_project_settings())
process.crawl(CorporateAnnouncementSpider)
process.start()