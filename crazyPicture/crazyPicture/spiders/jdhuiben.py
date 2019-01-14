# -*- coding: utf-8 -*-
'''
name = 'jdhuiben'
JD绘本图片
命令：scrapy crawl jdhuiben
'''
import scrapy
from crazyPicture.items import CrazypictureJDhuibenItem


class JdhuibenSpider(scrapy.Spider):
    name = 'jdhuiben'
    allowed_domains = ['search.jd.com', 'img10.360buyimg.com', 'img11.360buyimg.com', 'img12.360buyimg.com',
                       'img13.360buyimg.com', 'img14.360buyimg.com', 'img15.360buyimg.com']
    start_urls = ['http://www.jd.com/']

    search_url1 = 'https://search.jd.com/Search?keyword={key}&enc=utf-8&page={page}'
    num = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            # 'crazyPicture.pipelines.CrazypicturePipeline': 300,
            'crazyPicture.pipelines.CrazyPictureJDhibenPipline': 299,
        }

    }

    def start_requests(self):
        script = """
                function main(splash, args)
  splash:set_viewport_size(1028, 10000)
  splash:go(args.url)
  local scroll_to = splash:jsfunc("window.scrollTo")
  scroll_to(0, 2000)
  splash:wait(5)
  return {png=splash:png()}
end

                """

        # yield scrapy.Request(url=self.search_url1.format(key=key, page=2), callback=self.parse, dont_filter=True,meta={
        #     'dont_redirect':True,
        #     'splash':{
        #         'args': {'lua_source': script, 'images': 0},
        #         'endpoint': 'execute',
        #     }
        # })
        # yield scrapy.Request(url=self.search_url1.format(key='绘本', page=2), callback=self.parse, dont_filter=True,
        #                      meta={
        #                          'dont_redirect': True,
        #                          'splash': {
        #                              'args': {'lua_source': script},
        #                              'endpoint': 'execute',
        #                          }
        #                      })
        key = '绘本'
        for num in range(1, 100):
            page = str(2 * num - 1)  # 构造页数
            yield scrapy.Request(url=self.search_url1.format(key=key, page=page), callback=self.parse, dont_filter=True)
            # yield scrapy.Request(url=self.search_url1.format(key=key, page=page1), callback=self.get_next_half,meta={'page2': page2, 'key': key}, dont_filter=True)

    # def start_requests(self):
    #     script = """
    #             function main(splash)
    #                 splash:set_viewport_size(1028, 10000)
    #                 splash:go(splash.args.url)
    #                 local scroll_to = splash:jsfunc("window.scrollTo")
    #                 scroll_to(0, 2000)
    #                 splash:wait(15)
    #                 return {
    #                     html = splash:html()
    #                 }
    #             end
    #             """
    #
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.parse_info_index, meta={
    #             'dont_redirect': True,
    #             'splash': {
    #                 'args': {'lua_source': script, 'images': 0},
    #                 'endpoint': 'execute',
    #
    #             }
    #         })

    def parse(self, response):
        # text = response.text
        # with open('jdhiben.html', 'w') as f:
        #     f.write(text)
        #
        item = CrazypictureJDhuibenItem()
        for i in response.xpath(
                "//li[@class='gl-item']/div[@class='gl-i-wrap']/div[@class='p-img']/a/img/@source-data-lazy-img").extract():
            item['image_urls'] = i
            self.num += 1
            print('------' + str(self.num))
            yield item
