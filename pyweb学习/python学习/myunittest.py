import unittest,functools
from myclass import people
#填加一个装饰器用来打印日志
def mylog(func):
	@functools.wraps(func) #把func的信息保留下来
	def wrapper(*argvs,**kw) :
		print("this is ",func.__name__)
		func(*argvs,**kw)
		#return 1;
	return wrapper

class Testpeople(unittest.TestCase):
	#不能覆盖基类的构造函数 使用test__init__会覆盖基类的构造函数
	@mylog
	def test__init(self):  #测试构造函数能够顺利构造对象
		#unittest.TestCase.__init__(self) #可加可不加
		p1=people("LiLi",18,"girl")
		self.assertEqual(p1.name,"LiLi")  #测试值是否相等
		self.assertEqual(p1.sex,"girl")
	@mylog
	def test_setage(self):
		p1=people("LiLi",18,"girl")
		with self.assertRaises(ValueError):	#测试能够正确抛出异常
			p1.setage('two')
		pass
	def setUp(self):
		print("go  go  go jiang >-<")
	def tearDown(self):
		print("end")
if __name__ == '__main__':
	unittest.main()
