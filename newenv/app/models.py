#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)
#配置应用连接的数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/movie"
#追踪信号的修改并反馈
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db=SQLAlchemy(app) #定义db对象，实例化app连接关系型数据库数据库

"""定义表模型"""
#会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100), unique=True) #昵称
    pwd = db.Column(db.String(100)) #密码
    email = db.Column(db.String(100), unique=True) #邮箱
    phone = db.Column(db.String(11), unique=True) #手机号
    info = db.Column(db.Text) #个性简介
    face = db.Column(db.String(255), unique=True) #头像
    addtime =db.Column(db.DateTime, index=True,default=datetime.now) #注册时间
    uuid = db.Column(db.String(255), unique=True) #唯一标志符
    #会员日志表外键关系关联，
    userlogs =db.relationship('Userlog', backref='user')
    comments =db.relationship('Comment', backref='user')
    moviecols = db.relationship('Moviecol', backref='user')
    def __repr__(self):  #访问返回数据
        return "<User {}>".format(self.name)

#会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #引用外键
    ip =  db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return  "Userlog %r" %self.id

#标签
class Tag(db.Model):
    __tablename__= "tag"
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100), unique=True) #标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.now) #添加时间
    movies = db.relationship("Movie", backref='tag') #电影外键关系关联

    def __repr__(self):
        return  "Tag %r" %self.name
#电影
class Movie(db.Model):
    __tablename__ = "movie"
#    __table_args__ = {"useexisting": True}
 #   __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255))
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    start = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)   #播放量
    commentnum = db.Column(db.BigInteger) #评论量
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    comments = db.relationship("Comment", backref='movie') #关联表comment
    moviecols = db.relationship("Moviecol", backref='movie')
    def __repr__(self):
        return "Movie %r" % self.title

#上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Preview %r" % self.title

#评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    content = db.Column(db.Text)
    move_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Comment %r" % self.id

#电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    move_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Moviecol %r" % self.id

#权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)  #地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Auth %r" % self.name

#角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))   #权限
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    admins = db.relationship("Admin", backref='role')

    def __repr__(self):
        return "Role %r" % self.name

# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100), unique=True) #管理员账号
    pwd = db.Column(db.String(100)) #密码
    is_supper = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  #ForeignKey( ‘表名.列名’)或者(类名.成员)
    addtime =db.Column(db.DateTime, index=True,default=datetime.now) #注册时间
    adminlogs = db.relationship('Adminlog', backref='admin')
    oplogs = db.relationship('Oplog', backref='admin')

    def __repr__(self):  #访问返回数据
        return "<Admin {}>".format(self.name)

#管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id')) #引用外键
    ip =  db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return  "Adminlog %r" %self.id

#操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id')) #引用外键
    ip =  db.Column(db.String(100)) #管理员ip
    reason = db.Column(db.String(600)) #操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return  "Oplog %r" %self.id

def testrole():
    #测试能够插入数据
    role=Role(
        name=u'超级管理员',
        auths=""
    )
    db.session.add(role)
    db.session.commit()

def testadmin():
    # 测试能够插入数据
    from werkzeug.security import generate_password_hash
    admin = Admin(
        name = "cccmovie",
        pwd = generate_password_hash("ccc"),
        is_supper = 0,
        role_id = 1
    )
    db.session.add(admin)
    db.session.commit()


if __name__ == '__main__':
    #在mysql中创建数据库
    #db.create_all()

    #testrole()
    testadmin()
