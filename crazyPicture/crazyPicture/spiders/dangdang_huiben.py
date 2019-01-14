# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crazyPicture.items import CrazypictureJDhuibenItem


class DangdangHuibenSpider(CrawlSpider):
    name = 'dangdang_huiben'
    allowed_domains = ['book.dangdang.com', 'store.dangdang.com', 'baby.dangdang.com']
    start_urls = ['http://book.dangdang.com/children/01.41.43.htm?ref=book-01-A']
    num = 0
    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="/html/body/div[@id='bd']/div[@class='con '][6]/div[@id='13198']/div[@class='ppcbs ']/div[@class='con ']/ul[@id='component_map_id_2422642_part_id_']/li/a"),
            callback='parse_classes1', follow=True),
        Rule(LinkExtractor(allow="/\d+\?page_index=\d+#pos",
                           restrict_xpaths="/html/body/div[@id='bd_auto']/div[@class='con main']/div[@id='15182']/div[@class='qbsp_back ']/div[@class='con ']/div[@class='paginating show_spacer ']/div[@class='s_page']/a"),
             callback='parse_classes1', follow=True),
    )

    def parse_classes1(self, response):

        item = CrazypictureJDhuibenItem()
        for i in response.xpath(
                "/html/body/div[@id='bd_auto']/div[@class='con main']/div[@id='15182']/div[@class='qbsp_back ']/div[@class='con ']/div[@class='show_spacer ']/div[@class='con chuchuang']/ul/li/a[@class='pic']/img/@src").extract():
            item['image_urls'] = i
            self.num += 1
            print('++++++' + str(self.num))
            yield item

        for i in response.xpath("//img/@data-original").extract():
            item['image_urls'] = i
            self.num += 1
            print('------' + str(self.num))
            yield item




    def parse_test(self, response):
        self.num += 1
        print(self.num)
