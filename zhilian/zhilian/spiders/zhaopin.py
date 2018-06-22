# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from zhilian.items import ZhilianItem


class ZhaopinSpider(RedisCrawlSpider):
    name = 'zhaopin'
    allowed_domains = ['sou.zhaopin.com', 'jobs.zhaopin.com']
    redis_key = 'zhaopinspider:strat_urls'
    # start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=成都']
    rules = (
        Rule(LinkExtractor(allow=r'jl=.*?&sg=.*?&p=\d',),  follow=True),
        Rule(LinkExtractor(allow=r'http://jobs.zhaopin.com/.*?\.htm',),
             callback='parse_item', follow=False)
    )

    def __init__(self, *args, **kwargs):
        self.allowed_domains = ["sou.zhaopin.com", 'jobs.zhaopin.com']
        super(ZhaopinSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        itme = ZhilianItem()
        response = Selector(response)
        itme['职位月薪'] = response.re('职位月.*>([\u4e00-\u9fa5/\d-]+)')
        itme['发布日期'] = response.re('发布日期.*>([\d: -]+)')
        itme['工作地点'] = response.re('工作地点.*?>-([\u4e00-\u9fa5]+)')
        itme['工作性质'] = response.re('工作性质.*?>([\u4e00-\u9fa5]+)')
        itme['工作经验'] = response.re('工作经验.*?>([\u4e00-\u9fa5]+)')
        itme['最低学历'] = response.re('最低学历.*?>([\u4e00-\u9fa5]+)')
        itme['招聘人数'] = response.re('招聘人数.*?>([\u4e00-\u9fa5\d]+)')
        itme['职位类别'] = response.re('职位类别.*?>([\u4e00-\u9fa5]+)')
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return itme
