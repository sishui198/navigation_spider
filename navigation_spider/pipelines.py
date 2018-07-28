# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import Spider
from scrapy import Item
from navigation_spider.redis.ResidUtils import RedisClient


class NavigationSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class PrintPipline(object):

    def process_item(self, item, spider):
        print(item)
        return item

class FetchRedisQueuePipeline(object):

    def __init__(self, host: str, port: int, pwd: str, queue_name: str):
        self.host = host
        self.port = port
        self.pwd = pwd
        self.queue_name = queue_name

    @classmethod
    def from_crawler(self, crawler):
        return self(host=crawler.settings.get('REDIS_HOST'), port=crawler.settings.get('REDIS_PORT'), pwd=crawler.settings.get('REDIS_PWD'),
                    queue_name=crawler.settings.get('REDIS_QUEUE_NAME'))

    def open_spider(self, spider: Spider):
        self.redis = RedisClient(host=self.host, port=self.port, pwd=self.pwd)

    def process_item(self, item: Item, spider: Spider):
        self.redis.add(self.queue_name, item)
        return item
