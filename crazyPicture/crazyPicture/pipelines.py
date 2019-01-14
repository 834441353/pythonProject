# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
import time
import requests
from scrapy.utils.project import get_project_settings

from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

'''
class CrazypicturePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        #for image_url in item['image_urls']:
        print(item['image_urls'])
        yield Request(item['image_urls'])

    def item_completed(self,results,item,info):
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['images'] = image_path
        return item

'''


class CrazypicturePipeline(object):
    img_path = get_project_settings().get("IMAGES_STORE")

    def process_item(self, item, spider):
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',

        }

        if not os.path.exists(self.img_path):
            os.makedirs(self.img_path)
        # filename = self.img_path + int(time.time()*1000000)+'.jpg'

        filename = self.img_path + str(int(time.time() * 1000000)) + '.jpg'
        with open(filename, 'wb') as f:
            req = requests.get(item['image_urls'], headers=header)
            # req = requests.get('http:'+item.get('image_urls'), headers=header)
            f.write(req.content)
        return item

#
class CrazyPictureJDhibenPipline(object):
    img_path = get_project_settings().get("IMAGES_JDHUIBEN_STORE")

    def process_item(self, item, spider):
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',

        }

        if not os.path.exists(self.img_path):
            os.makedirs(self.img_path)
        # filename = self.img_path + int(time.time()*1000000)+'.jpg'

        filename = self.img_path + str(int(time.time() * 1000000)) + '.jpg'
        with open(filename, 'wb') as f:
            # req = requests.get(item['image_urls'], headers=header)
            req = requests.get('http:' + item.get('image_urls'), headers=header)
            f.write(req.content)
        return item