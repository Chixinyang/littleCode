#coding :utf-8
'''注册蓝图'''
from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint) #前台不需要指定url前缀
app.register_blueprint(admin_blueprint,url_prefix="/admin")