#coiding:utf-8

from urllib import request
import chardet

myurl = 'http://www.gnz48.com/nongyanping/support.html'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; 1503-M02 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN'
req = request.Request(url = myurl, headers = head)
res = request.urlopen(req)
myhtml = res.read()
charset = chardet.detect(myhtml) #获取网页编码方式
#print("编码方式 ：",charset)
download_html=myhtml.decode(charset['encoding'],'ignore') #忽略掉转码失败部分
with open('应援.html', 'w', encoding='utf-8')  as file :
    file.write(download_html)