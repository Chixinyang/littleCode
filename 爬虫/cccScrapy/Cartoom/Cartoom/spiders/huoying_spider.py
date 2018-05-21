# -*- coding:UTF-8 -*-
import scrapy

"""
在cmd中使用如下指令运行工程：
            scrapy crawl name
"""
class huoyingSpider(scrapy.Spider):

    name = "huoying"    #自己定义的内容，在运行工程的时候需要用到的标识；
    allowed_domains = ['comic.kukudm.com']  #允许爬虫访问的域名，防止爬虫跑飞。让爬虫只在指定域名下进行爬取，值得注意的一点是，这个域名需要放到列表里；
    start_urls = ['http://comic.kukudm.com/comiclist/3/']   #开始爬取的url，同样这个url链接也需要放在列表里；

    def parse(self, response):  #请求分析的回调函数，如果不定义start_requests(self)，获得的请求直接从这个函数分析；
        link_urls = response.xpath('//dd/a[1]/@href').extract()
        for each_link in link_urls:
            print('http://comic.kukudm.com' + each_link)   #获取每个章节的url

car=huoyingSpider()
car.parse()