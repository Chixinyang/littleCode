import sys
class Animal(object):
	counter=0  #类变量
	def __init__(self):
		Animal.counter +=1   #操作类变量
		self.counter=0   	#定义并初始化成员变量
	def run(self):
		print('Animal is running... ',Animal.counter," ",self.counter)

class Cat(Animal):
	def __init__(self):
		Animal.__init__(self);
	def run(self):
		print('Cat is running...',Animal.counter," ",self.counter)

class Timer(object):
    def run(self):
        print('Start...')
def run(animal):
    animal.run()

run(Animal())
run(Cat())
run(Timer())