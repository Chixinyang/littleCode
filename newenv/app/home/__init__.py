# codiing:utf-8

'''定义蓝图'''
from flask import Blueprint
home=Blueprint("home",__name__)  #home是一个蓝图
import app.home.views   #导入蓝图的路由方法