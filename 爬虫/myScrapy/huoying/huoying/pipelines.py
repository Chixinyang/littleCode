# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#    清理HTML数据
#    验证爬取的数据(检查item包含某些字段)
#    查重(并丢弃)
#    将爬取结果保存到数据库中

from huoying import settings
from scrapy import Request
import requests
import os

class HuoyingPipeline(object):
    def process_item(self, item, spider):
        #如果获取了图片链接，进行如下操作
        if 'img_url' in item:
            images = []
            #文件夹名字
            dir_path = '%s/%s' % (settings.IMAGES_STORE, item['dir_name'])
            #文件夹不存在则创建文件夹
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            #获取每一个图片链接
            for image_url in item['img_url']:
                #解析链接，根据链接为图片命名
                houzhui = image_url.split('/')[-1].split('.')[-1]
                qianzhui = item['link_url'].split('/')[-1].split('.')[0]
                #图片名
                image_file_name = '第' + qianzhui + '页.' + houzhui
                #图片保存路径
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue
                #保存图片
                with open(file_path, 'wb') as handle:
                    response = requests.get(url = image_url)
                    #图片大小
                    #content_size = int(response.headers['content-length'] 
                    #从响应中每次获取1024kb
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
            #返回图片保存路径
            item['image_paths'] = images
        return item