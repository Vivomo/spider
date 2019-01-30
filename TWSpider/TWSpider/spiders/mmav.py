# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

class MmavSpider(scrapy.Spider):
    name = 'mmav'
    allowed_domains = ['702rr.com']
    start_urls = ['https://702rr.com/index/home.html']

    def parse(self, response):
        category = response.css('.row-item-content')
        img_category = category[2]
        img_url = img_category.css('a')
        for node in img_url:
            url = node.css('::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)
        pass

    def parse_detail(self, response):

        pass