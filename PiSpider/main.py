from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PiSpider.transmission import *
import time

debug = 0
if debug:
    import yaml
    import re
    with open("PiSpider/config.yml","r", encoding="utf8") as refile:
        cfg = yaml.load(refile)
    my_spider = cfg['dmhy_rss_spider']
    #print (my_spider)
    re_list = my_spider['re']
    name = my_spider['name']
    test_str = '<![CDATA[ 【DMHY】【黑色五葉草/Black_Clover】[78][繁體][720P][MP4] ]]>'
    for re_rule in re_list:
        result =  re.findall(re_rule, test_str)
        if len(result) != 0:
            print (re_rule)
            print (result)         
    exit()

if __name__=="__main__":

    #remove_transmission_finish_work()
    process = CrawlerProcess(get_project_settings())
    process.crawl('dmhy_rss')
    process.start() # the script will block here until the crawling is finished



