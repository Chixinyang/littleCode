import sys
from sqlalchemy import Column,Integer,String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#print(dir(sqlalchemy)) #检测模块是否导入成功
#创建基类
Base=declarative_base()
#定义需要表格的对象

class ccc (Base) :
	__tablename__='ccc'; #table name 
	#表的结构
	id=Column(Integer,primary_key = True ) ;  #使用的变量类型一定要从sqlalchemy中导入到工作空间
	name=Column(String(20));
# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/cxy')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)  #创建链接会话类型
# 创建session对象:
session = DBSession() 
# 创建新User对象:
new_user = ccc(id=5, name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
user = session.query(ccc).filter(ccc.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭session:
session.close()

