# -*- coding: utf-8 -*-
import scrapy


class ComixSpider(scrapy.Spider):
    name = 'comix'
    allowed_domains = ['twcomix.com']
    start_urls = ['http://twcomix.com/taglist']

    def parse(self, response):
        pass
