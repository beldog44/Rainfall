# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import WebItem
from scrapy.linkextractors import LinkExtractor

class WebSpiderSpider(scrapy.Spider):
    name = "webspiderSpider"
    allowed_domains = ["http://www.data.jma.go.jp/"]
    start_urls = ['http://www.data.jma.go.jp/obd/stats/etrn/view/10min_s1.php?prec_no=62&block_no=47772&year=2017&month=3&day=1&view=a4']

    def parse(self, response):
       article = WebItem()
       article['name'] = response.css("td.data_0_0").extract_first()
       yield article
