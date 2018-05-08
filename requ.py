import requests

s= requests.Session()
c = requests.cookies.RequestsCookieJar()  
#c.set('cookie-name', 'cookie-value', path='/', domain='.abc.com') 
#c.set('"PHPSESSID","306b06a34ff67309ff9bd7d0da1e200b"')
#s.cookies.update(c)
s.cookies['PHPSESSID'] = '306b06a34ff67309ff9bd7d0da1e200b'
url = 'https://www.baidu.com/'
headers = {'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
}
req = s.get(url=url,headers=headers)
print(type(req))