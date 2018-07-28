# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NavigationSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WxAppStoreItem(scrapy.Item):

    url = scrapy.Field() # 响应 url
    json_data = scrapy.Field() # 返回的 json 数据