import sys
class people :
	def __init__(self,name,age,sex):
		self.name=name
		self.__age =age  #age被定义成私有成员
		self.sex =sex
	def info(self):
		print('this is {0},a {1}-year-old {2}'.format(self.name,self.__age,self.sex))
		pass
	def __str__(self):    #类的专有方法之一，功能是重载print,要返回一个string
		return str('this is {0},a {1}-year-old {2}'.format(self.name,self.__age,self.sex))
		pass
	def getage(self) :
		return self.__age;
	def setage(self,newage):
		if  not(isinstance(newage,int)) :
			raise ValueError("newage should be int")
		else:
			self.__age=newage
class employee (people):
	def __init__(self,name,age,sex,company) :
		self.company=company
		#people.__init__(self,name,age,sex)
		super().__init__(name,age,sex)  #使用super可以省掉self这个参数
	def info(self):
		print('this is {0},a {1}-year-old {2} working in {3}'
				.format(self.name, self.getage(), self.sex, self.company) #子类不能访问基类的私有成员
			)
		pass
if __name__ == '__main__' :
	p1=people("LiLi",18,"girl")
	p1.info();
	print(p1) # 应为p1重载过print所以能直接通过print打印，若为重载打印的是乱码
	#print( p1.name," is ",p1.__age) #不能直接访问私有成员
	p2=employee("张飞",19,"man","ZteSoft")
	p2.info()
	super(employee,p2).info(); # super(子类，子类对象).父类成员函数  ---实现子类对覆盖的父类成员函数的调用
