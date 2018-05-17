# -*- coding: UTF-8 -*-
from urllib import request
import chardet
if __name__ == "__main__":
    #访问网址
    url = 'http://ip.xianhua.com.cn/'
    #这是代理IP
    proxy = {'http':'123.138.89.133:9999'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener,安装后会修改urlopen的ip地址
    #request.install_opener(opener)
    #使用自己安装好的Opener
    #response = request.urlopen(url)
    #避免对urlopen的修改
    response = opener.open(url)
    #读取相应信息并解码
    html = response.read()  #.decode("utf-8")
    charset = chardet.detect(html) #获取网页编码方式
    print("编码方式 ：",charset)
    html=html.decode(charset['encoding'])
    #打印信息
    print(html)