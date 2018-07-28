from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PiSpider.transmission import *
process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
process.crawl('dmhy_rss')
process.start() # the script will block here until the crawling is finished
remove_transmission_finish_work()
