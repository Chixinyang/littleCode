import random, time, queue,os
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
# 发送任务的队列:
task_queue = queue.Queue() #创建类的对象
print("task_queue type is :",type(task_queue))
#task_queue = queue()
# 接收结果的队列:
result_queue = queue.Queue()
#result_queue = queue()
# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):   #定义自己的队列管理类
    pass
'''
在创建多进程时linux支持fork()不需要考虑序列化的问题，而Windows没有fork调用，需要考虑序列化的问题
multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
linux通过fork拷贝父进程，windows是创建一个新的进程，然后把它进行阉割成子进程，而且它必须运行由管道传递的代码，
freezesupport()它的任务是检查它所运行的进程是否应该运行由管道传递的代码。
'''
# 把队列注册到网络上（ip,port）
# 把队列添加子进程中，使用callable参数关联Queue对象,第一个参数表示返回这个队列的方法，只提供名字即可
#QueueManager.register('get_mytask',callable=task_queue) #
#QueueManager.register('get_myresult',callable=lambda :result_queue)#pikle 不支持匿名函数
def return_task_q():
	global task_queue
	return task_queue
def return_result_q():
	global result_queue
	return result_queue
QueueManager.register('get_mytask',callable=return_task_q ) 
QueueManager.register('get_myresult',callable=return_task_q)
# 绑定ip和端口5000, 设置验证码'abc'  ，返回一个完整的管理类对象:
# linux 的默认ip是127.0.0.1  window必须手动添加ip
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')  #返回一个进程对象
print("manager type is :",type(manager))
print("current pid is {}".format(os.getpid()) )
#必须要显示的指出初始进程是主进程，下面代码只有父进程才会执行，上面的子进程也会执行一遍
if __name__ == '__main__' :
	freeze_support() 
	print("ok")
	# 启动Queue: 
	manager.start() #子进程启动，只有启动后才能在网络以及本地上访问
	# 获得通过网络访问的Queue对象:
	# 本地通过管理类对象manger访问队列，而不要直接用最原始的队列名字task_queue访问，因为那样就失去了包裹的意义
	task = manager.get_mytask()
	result = manager.get_myresult()
	print("task type is :",type(task) )
	flag = 0
	task.put(flag)
	# 从result队列读取结果:
	print(flag)
	print('Try get results...')
	while flag != 1 :
		flag=result.get(timeout=10) #队列取出消息后 ，长度减1；所以主进程如果先取出数据的话，队列中就没有数据了，需要重新写入
		task.put(0) #
		print(flag)
		pass
	#关闭:
	manager.shutdown()
	print()
	print('master exit.')
