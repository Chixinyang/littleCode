import sys,os,time
from multiprocessing import Process  #导入进程类
def testpro(delayt):
	print("pid is :",os.getpid()," now is :",time.ctime())
	time.sleep(delayt)
	print("end time is :",time.ctime())
if __name__ == '__main__':
	print("start Process")
	p=Process(target=testpro,args=(5,) )#定义进程对象
	p.start()
	p.join()
	print("end Process")
