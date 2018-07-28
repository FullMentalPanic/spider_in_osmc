from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PiSpider.transmission import *
import time


# 'followall' is the name of one of the spiders of the project.
process = CrawlerProcess(get_project_settings())
process.crawl('dmhy_rss')
process.start() # the script will block here until the crawling is finished
remove_transmission_finish_work()
#time.sleep(12*60*60)
