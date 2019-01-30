# -*- coding: utf-8 -*-
import scrapy


class ComixSpider(scrapy.Spider):
    name = 'comix'
    allowed_domains = ['twcomix.com']
    start_urls = ['http://twcomix.com']
    # start_urls = ['http://baidu.com']

    headers = {
        "HOST": "twcomix.com",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": 1,
        # "Referer": "http://twcomix.com/hentai_manga/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    }

    def parse(self, response):
        pass
