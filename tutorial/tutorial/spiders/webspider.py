# -*- coding: utf-8 -*-
import scrapy
import datetime
from datetime import date
from tutorial.items import WebItem
from scrapy.linkextractors import LinkExtractor

class WebSpiderSpider(scrapy.Spider):
    name = "webspiderSpider"
    allowed_domains = ["http://www.data.jma.go.jp/"]
    d1 = date(2017, 3, 29)                #調査年月日
    dd1 = (d1.day)                        #調査日付のみ
    #d = datetime.date(20:16, 6, 27)
    d2 = date(2017, 3, 31)                #調査最終年月日
    #print (d1)
    #td = datetime.timedelta(days=1)  #for文で回るようにする
    while d1 <= d2:
        print ('start')
        #dd1 = (d1.day)                #繰り返す度に日付を更新するため
        #dd1 = (d1.day)
        start_urls = ['http://www.data.jma.go.jp/obd/stats/etrn/view/10min_s1.php?prec_no=62&block_no=47772&year=2017&month=03&day={0}&view=a4'.format(dd1)]
        d1 = d1 + datetime.timedelta(days = 1)
        dd1 = (d1.day)
   # else:
    #    print ('end')

        def parse(self, response):
          article = WebItem()
          article['time']  = response.xpath('//td/text()').extract()
       # article['time']  = response.css("td.white-space:nowrap").extract_first()
       #article['name'] = response.css("td.data_0_0").extract_first()
          yield article
    
    else:
        print ('end')
