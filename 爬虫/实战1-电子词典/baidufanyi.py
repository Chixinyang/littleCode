#coding=utf8
 
import hashlib
import requests
import random

def GetMd5( mystr):      
    md5 = hashlib.md5()
    md5.update(mystr.encode('utf-8'))
    return(md5.hexdigest())

def translater(q,fromLang='auto',toLang='zh'):   
    appid = '20180513000158033'
    secretKey = 'jTQsUh8XT5zpKWCdZFrT'

    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    #fromLang = 'en'  #可以为auto
    #toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    sign = GetMd5(sign)
    data = {"appid":appid,"q":q,"from":fromLang,"to":toLang,"salt":str(salt),"sign":sign}
    resp=requests.get(myurl,data).json()
    reslut=resp['trans_result'][0]
    #print("{0} 结果是 {1}".format(reslut['src'],reslut['dst']))
    return(reslut['dst'])

if __name__ == "__main__":
    translater('apple')