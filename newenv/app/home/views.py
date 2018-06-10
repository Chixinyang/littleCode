#coding:utf-8

'''调用蓝图'''
'''定义url的处理函数'''
from . import home
@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"
