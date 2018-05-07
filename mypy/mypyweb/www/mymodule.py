#-*- coding:utf-8 -*-

'''
 Modules for user,blog,comment
 用类描述数据库的表
'''
__author__="Chixinyang"

import time,uuid

from myorm import IntegerField,StringField,DateTimeField,TextField,Model,BooleanField,FloatField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

 #在类的级别上定义对象和表的映射关系
class users(Model):
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)',default='')
    passwd = StringField(ddl='varchar(50)',default='')
    admin = BooleanField(default=0)
    name = StringField(ddl='varchar(50)',default='')
    image = StringField(ddl='varchar(500)',default='')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
