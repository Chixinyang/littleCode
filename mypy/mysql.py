import sqlite3 #导入sqllist3 模块
#定义一个lambda，检查变量是否存在，如果存在打印类型
check= lambda x : print("success ,it`s type is ",type(x) ) if x else print("failed") 
showlist= lambda l : print("list内容是：",l) if type(l)==list else print("error")
#db=sqlite3.connect('test.db') #链接或创建数据库

import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",db="cxy") 
check(db)
cursor=db.cursor(cursor=pymysql.cursors.DictCursor) #创建一个字典游标，通过游标操作数据库，默认游标是元组类型
check(cursor)
try :
	"""cursor.execute('''create table ccc 
					(	id int primary key,
						name  varchar(20) )
					''') #创建表ccc
	"""
	#cursor.execute("insert into ccc (id ,name ) values(3,'ccc')") #向表中插入数据
	print("本次插入到 {} 表的行数是：{}".format( 'ccc',cursor.rowcount) )  #查看本次插入的行数	
	#查询表ccc 并取出所有的查询结果并打印
	#sqlite3 查询返回的是查询的数据，mysql查询返回的是结果的数量
	values=cursor.execute("select * from {0} ".format('ccc'))
	check(values)
	values=cursor.fetchall()
	#showlist(values) #打印查询结果 
	check(values)
	print(values)
	db.commit() 	#提交事务
except (pymysql.err.ProgrammingError,AttributeError,pymysql.err.InternalError
		,pymysql.err.IntegrityError) as err:
	print("db error :",err)
finally:
	cursor.close()   #关闭游标
	db.close()		#关闭数据库
