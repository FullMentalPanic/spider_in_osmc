# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
from scrapy import log
import codecs
from datetime import datetime
from hashlib import md5
from PiSpider.transmission import Transmission_control
import PiSpider.settings as settings

class DmhyRSSPipeline(object):
    def open_spider(self, spider):
        self.queue = []
        self.file = codecs.open('/' + spider.name+'.txt','r+')
        for line in self.file:
            self.queue.append(line)
        self.rpc = Transmission_control()

    def close_spider(self, spider):
        self.file.seek(0)
        for md5 in self.queue:
            self.file.write(md5)
        self.rpc.remove_finish_torrent()
        self.rpc.close()

    def process_item(self, item, spider):
        linkmd5id = self._get_linkmd5id(item) + '\n'
        if linkmd5id not in self.queue:
            if len(self.queue) >= 100:
                self.queue.pop(0)
            self.queue.append(linkmd5id)
            self.rpc.download_torrent(str(item['magnet']),str(item['location']))
        else:
            pass
        return item

    def _get_linkmd5id(self, item):
        return md5(str(item['magnet']).encode('utf-8')).hexdigest()

    def _handle_error(self, failue, item, spider):
        log.err(failure)
