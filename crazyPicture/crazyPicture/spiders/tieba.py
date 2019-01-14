# -*- coding: utf-8 -*-
import scrapy
#from lxml import etree
from crazyPicture.items import CrazypictureItem

class TiebaSpider(scrapy.Spider):
	name = 'tieba'
	allowed_domains = ['tieba.baidu.com']
	#start_urls = ['https://tieba.baidu.com']
	url = 'http://tieba.baidu.com'
	start_urls = [url+'/f/index/forumclass']
	tem_url = ''
	tem = 1
	wqer = 0

	def parse(self, response):
		#查询全部贴吧分类
		'''
		for i in response.xpath('//ul[@class="item-list-ul clearfix"]/li/a/@href').extract():
			self.tem_url = i
			yield scrapy.Request(self.url+i,callback=self.load_item_page)
		'''
		#单个分类的贴吧
		self.tem_url = response.xpath('//ul[@class="item-list-ul clearfix"]/li/a/@href').extract()[0]
		yield scrapy.Request(self.url+response.xpath('//ul[@class="item-list-ul clearfix"]/li/a/@href').extract()[0],callback=self.load_item_page)
		
		'''
    	print(etree.HTML(response.body).xpath('//div[@class="thread-name-wraper"]/a/@href'))
    	print('--------------------------')

    	print(response.xpath('//div[@class="thread-name-wraper"]/a/@href').extract())

    	
    	with open('tieba.html','wb') as f:
    		f.write(response.body)
    		f.close()
    	
    	href_list = etree.HTML(response.body).xpath('//div[@class=thread-name-wraper]/a/@href')
    	with open('as.txt','w') as f:
    		f.write(str(href_list))
    		f.close()
		'''
	def load_item_page(self,response):
		print(response.xpath('//div[@class="ba_info ba_info2"]/a/@href | //div[@class="ba_info"]/a/@href').extract())
		for each in response.xpath('//div[@class="ba_info ba_info2"]/a/@href | //div[@class="ba_info"]/a/@href').extract():
			tieba_url = self.url+each
			yield scrapy.Request(tieba_url,callback = self.load_itemitem)
		print(response.xpath('//div[@class="pagination"]/a[@class="next"]/text()').extract())
		if response.xpath('//div[@class="pagination"]/a[@class="next"]/text()').extract()==['下一页>']:
			self.tem+=1
			page = '&st=new&pn='+str(self.tem)
			print('```````````````````````````````````````````````````````')
			print(self.url+self.tem_url+page)
			yield scrapy.Request(self.url+self.tem_url+page,callback=self.load_item_page)
			
		
		
		'''
		if  response.xpath('//div[@class="pagination"]/a[@class="next"]')!=[]:

			#每个贴吧的url
			for each in response.xpath('//div[@class="ba_info ba_info2"]/a/@href | //div[@class="ba_info"]/a/@href').extract():
				tieba_url = self.url+each
				yield scrapy.Request(tieba_url,callback = self.load_itemitem)
		'''
		
	def load_itemitem(self,response):
		for each in response.xpath('//a[@class="j_th_tit "]/@href').extract():
			tiezi_url = self.url+each
			yield scrapy.Request(tiezi_url,callback=self.load_itemImg)
		

	def load_itemImg(self,response):
		item = CrazypictureItem()
		for each in response.xpath('//img[@class="BDE_Image"]/@src').extract():
			item['image_url'] = each
			print('---------'+each)
			yield item