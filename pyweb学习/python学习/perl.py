import sys,re
str="ztesoftID:0027010038@cxy13579.cn";
myrule=r'(\w+)(:)(\d+)(@)([a-z]+\d+)(\.\w+)'
myrule=r'([\w\d\_]+@[\w\d]+.(com|cn)$)' 
m1=re.match(myrule,str);  #从头开始匹配
print("m1= ",m1)
m2=re.search(myrule,str).groups(); #查看整个字符串,加上括号就是把匹配的字符串保存成一个元组成员
print("m2= ",m2)
m3=re.match(r'^(\d+)(0*)$', '102300').groups() #贪婪匹配，也就是匹配尽可能多的字符，满足表达式1就可以
print(m3) 
m3=re.match(r'^(\d+?)(0*)$', '102300').groups() #非贪婪匹配，也就是匹配尽可能少的字符，
												#在满足表达式1时会考虑是否满足表示2
print(m3)
'''
import os
print ("Content-type: text/html")
print ()
print ("<meta charset=\"utf-8\">")
print ("<b>环境变量</b><br>")
print ("<ul>")
for key in os.environ.keys():
    print ("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print ("</ul>")
'''