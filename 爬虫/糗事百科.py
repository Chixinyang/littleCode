# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def DisplayTypeOrContent( tag ,varname, ShowContentFlag = False):
    print("type of {} is {}:".format( varname,type(tag) ) )
    if  ShowContentFlag == True :
        print(tag)
    

url=r"https://www.qiushibaike.com/hot/page/1/"
header= {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
s=requests.Session()
resp = s.get(url = url , headers = header) 
DisplayTypeOrContent(resp,"resp")

html = resp.text # 通过text提取html页面
DisplayTypeOrContent(html,"html")

bf = BeautifulSoup(html, 'lxml')
res_cont = bf.find_all('div',class_="col1")
DisplayTypeOrContent(res_cont,"res_cont",True) 

bf_cont=BeautifulSoup(str(res_cont),'lxml')

for item_bf in bf_cont.contents[0].contents:
    if item_bf.find_all('div',class_="thumb") != [] :
        print('a img')
        #print(item_bf.text)
    else :
        print(item_bf.text)
