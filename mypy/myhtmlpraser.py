from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import functools
def funcname(func):
    @functools.wraps(func)
    def wrapper(*argvs,**kv):
      #  print("this is func :",func.__name__)
        func(*argvs,**kv)
      #  print("end func     :",func.__name__)
    return wrapper

class MyHTMLParser(HTMLParser):
    def __init__(self,*argvs,**kv) :
        self.trgs=['']*6;
        self.flag=[False,True];
        self.event=[];
        self.events=[];
        super().__init__(*argvs,**kv)
    @funcname
    def handle_starttag(self, tag, attrs): #处理开始标签
       # print('<%s>' % tag)
        if 'ul'==tag :
            #self.trgs=['']*6;
            self.flag[0]= True
        if True==self.flag[0] and True==self.flag[1]:
            if 'li'==tag:
                self.trgs[0]=tag
            elif 'h3'==tag and self.trgs[0]=='li':
                self.trgs[1]=tag
            elif 'a' ==tag and self.trgs[1]=='h3':
                self.trgs[2]=tag
            elif 'time' ==tag and 'a'==self.trgs[2]:
                self.trgs[3]=tag
            elif 'span' ==tag and 'span' != self.trgs[4]:
                self.trgs[4]=tag
            if 'span' ==tag and 'span'==self.trgs[4] :
                self.trgs[5]=tag

    @funcname
    def handle_endtag(self, tag):         #处理结束标签
        print('</%s>' % tag)
        if 'ul' == tag and not(self.events == []):
            self.flag[1]=False
    @funcname
    def handle_startendtag(self, tag, attrs): 
        print('<%s/>' % tag)
    @funcname
    def handle_data(self, data):
        print(data)
        data=data.replace(r'\n','').strip()
        if 'a'   ==self.trgs[2] and self.trgs[3]=='':
            self.event.append(data)
        if 'time'==self.trgs[3] and self.trgs[4]=='':
            self.event.append(data)
        if 'span'==self.trgs[4] and self.trgs[5]=='':
            self.event.append(data)
        if 'span'==self.trgs[5] :
            self.event.append(data)
            self.events.append(self.event)
            self.trgs=['']*6;
            self.event=[]
    @funcname
    def handle_comment(self, data):
        print('<!--', data, '-->')
    @funcname
    def handle_entityref(self, name):
        print('&%s;' % name)
    @funcname
    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
url=r'https://www.python.org/events/python-events/'
with request.urlopen(url, timeout=4) as f:
    data = f.read()   
    print("date type is :",type(data))
    parser.feed(str(data))
    print(">>>>>>>>>>>",parser.events)