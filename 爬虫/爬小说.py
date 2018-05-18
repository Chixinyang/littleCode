# -*- coding:UTF-8 -*-
from urllib import request

import chardet
from bs4 import BeautifulSoup


def GetOneLesssion():
    download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url = download_url, headers = head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read()

    charset = chardet.detect(download_html) #获取网页编码方式
    #print("编码方式 ：",charset)
    download_html=download_html.decode(charset['encoding'],'ignore') #忽略掉转码失败部分

    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id = 'content', class_ = 'showtxt') #提取指定标签的信息


    soup_text = BeautifulSoup(str(texts), 'lxml') #将标签和内容转成 beautifusoup对象
    #novel=soup_text.div.text #提取soup内的文本内容
    #print(novel)
    #将\xa0无法解码的字符删除
    #print(soup_text.div.text.replace('\xa0',''))
    import re
    print( re.sub(r'\s\s+',r'\n    ',soup_text.div.text) )  #把多个空格转变成换行符，中文段落格式，一个中文字符两个字节

def GetCatalogue():
    target_url = 'http://www.biqukan.com/1_1094/'  #小说目录url
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    begin_flag = False
    #计算章节个数
    #numbers = (len(download_soup.dl.contents) - 1) / 2
    #print("总计章节：",int(numbers) )
    #获取最新章节数
    newcont=download_soup.dl.contents[3].string
    import re
    myre=re.compile(r'\d{1,4}') #从文字中提起当前章节数
    numbers=myre.search(newcont).group()
    print("最新章节{0} ：{1},".format(numbers,newcont))
    
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤除回车
        if child != '\n':
            #找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            #爬取链接
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_name = child.string
                #print(download_name + " : " + download_url)
def GetNovel():
    # -*- coding:UTF-8 -*-
    from urllib import request
    from bs4 import BeautifulSoup
    import re
    import sys
    #创建txt文件
    file = open('一念永恒.txt', 'w', encoding='utf-8')
    #一念永恒小说目录地址
    target_url = 'http://www.biqukan.com/1_1094/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    #计算章节个数
    newcont=download_soup.dl.contents[3].string
    import re
    myre=re.compile(r'\d{1,4}') #从文字中提起当前章节数
    numbers=myre.search(newcont).group()
    index = 1
    #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    begin_flag = False
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤除回车
        if index >= 10 :
            break
        if child != '\n':
            #找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            #爬取链接并下载链接内容
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')  #获取章节url
                download_req = request.Request(url = download_url, headers = head) #访问章节的url
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')
                download_name = child.string
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                write_flag = True
                file.write(download_name + '\n\n')
                #将爬取内容写入文件
                for each in soup_text.div.text.replace('\xa0',''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != ' ':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                file.write('\n\n')
                #打印爬取进度
                sys.stdout.write("已下载:%.3f%%" % float(index/int(numbers) ) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()

def CxyGetNovel():
    from urllib import request
    from bs4 import BeautifulSoup
    import re
    import sys
    #创建txt文件
    file = open('ccc一念永恒.txt', 'w', encoding='utf-8')
    #一念永恒小说目录地址
    target_url = 'http://www.biqukan.com/1_1094/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    #计算章节个数
    newcont=download_soup.dl.contents[3].string
    myre=re.compile(r'\d{1,4}') #从文字中提起当前章节数
    numbers=myre.search(newcont).group()
    index = 1
    #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    begin_flag = False
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤除回车
        '''
        #下载测试
        if index >= 10 :
            break
        '''
        if child != '\n':
            #找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            #爬取链接并下载链接内容
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')  #章节url
                download_req = request.Request(url = download_url, headers = head) 
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')  #章节页面
                download_name = child.string  #章节的名字
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                newtext = re.sub(r'\s\s+',r'\n    ',soup_text.div.text)  #对内容排版 
                write_flag = True
                file.write(download_name + '\n\n') #把章节名字写入文本
                #将爬取内容写入文件
                '''
                for each in soup_text.div.text.replace('\xa0',''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != ' ':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                '''
                file.write(newtext)
                file.write('\n\n')
                #打印爬取进度
                sys.stdout.write("已下载:%.3f%%" % float(index/int(numbers) ) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()
  
if __name__ == '__main__':
    CxyGetNovel();
