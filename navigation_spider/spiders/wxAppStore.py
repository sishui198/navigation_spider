# -*- coding: utf-8 -*-
import scrapy
import json
from navigation_spider.items import WxAppStoreItem


base_url = "http://www.160.com/xiaochengxu/"

base_item = ['gouwu', 'gongju', 'jiaoyu', 'canyin', 'meiti', 'jiaotong', 'shenghuofuwu', 'shejiao', 'lvyou', 'zwms']

pages = ['1', '2', '3']

DEFAULT_REQUEST_HEADERS = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'www.160.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


class WxappstoreSpider(scrapy.Spider):
    name = 'wxAppStore'
    allowed_domains = ['www.160.com']

    def start_requests(self):
        params = '?act=1'
        for item in base_item:
            DEFAULT_REQUEST_HEADERS['Referer'] = base_url+item+"/index.html"
            for page in pages:
                url = base_url+item+"/"+page+params
                yield scrapy.Request(url, self.parse, headers=DEFAULT_REQUEST_HEADERS)



    def parse(self, response):
        result = json.loads(response.text)
        url = response.url
        if(result['result'] == 1):
            for list in result['list']:
                item = WxAppStoreItem()
                item['url'] = url
                item['json_data'] = list
                yield item


