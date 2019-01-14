# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crazyPicture.items import CrazypictureItem

class TiebaCrawlSpider(CrawlSpider):
    name = 'tieba_crawl'
    allowed_domains = ['tieba.baidu.com','imgsa.baidu.com']
    url = 'http://tieba.baidu.com'
    start_urls = [url+'/f/index/forumclass']
    #start_urls = ['http://tieba.baidu.com/f?kw=akb48']
    num = 0
    #pagelink = LinkExtractor(restrict_xpaths=('//ul[@class="item-list-ul clearfix"]/li/a/@href'))
    pagelink = LinkExtractor(allow=('/f/index/forumpark\?cn=\S+'))
    tiebalink = LinkExtractor(allow=('/f\?kw=\S+'))
    tiezilink = LinkExtractor(allow=('/p/\d+'))
    rules = (
        Rule(pagelink, follow=True),
        Rule(tiebalink, follow=True),
        Rule(tiezilink, callback='parse_tiezi', follow=True),
    )
    def parse_tiezi(self,response):
        item = CrazypictureItem()
        for each in response.xpath('//img[@class="BDE_Image"]/@src').extract():
            item['image_urls'] = each
            self.num+=1
            print('---------'+str(self.num))
            yield item
