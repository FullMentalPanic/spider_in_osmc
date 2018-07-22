## -*- coding: utf-8 -*-
# get magnet from target web
import scrapy
from PiSpider.items import *
import yaml
import re

class dmhyspider(scrapy.Spider):
    name = "dmhy_rss"
    start_urls = [
        'https://share.dmhy.org/topics/rss/rss.xml',
    ]

    def parse(self, response):
        with open("PiSpider/config.yml","r", encoding="utf8") as refile:
            cfg = yaml.load(refile)
        my_spider = cfg['dmhy_rss_spider']
        #print (my_spider)
        re_list = my_spider['re']
        name = my_spider['name']
        item = PispiderItem()
        for rss in response.xpath("//item"):
            title = rss.xpath(".//title/text()").extract_first()
            count = 0
            for re_rule in re_list:
                if re.search(re_rule, title) is not None:
                    item['title'] = title
                    item['location'] = name[count]
                    item['magnet'] = rss.xpath(".//enclosure/@url").extract_first()
                    yield item
                else:
                    pass
                count = count + 1
