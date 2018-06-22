# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    职位月薪 = scrapy.Field()
    发布日期 = scrapy.Field()
    工作地点 = scrapy.Field()
    工作性质 = scrapy.Field()
    工作经验 = scrapy.Field()
    最低学历 = scrapy.Field()
    招聘人数 = scrapy.Field()
    职位类别 = scrapy.Field()
