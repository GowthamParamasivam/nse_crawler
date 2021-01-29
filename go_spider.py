from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from nse_crawler.spiders.CorporateAnnouncement import CorporateAnnouncementSpider


process = CrawlerProcess(get_project_settings())
process.crawl(CorporateAnnouncementSpider)
process.start()