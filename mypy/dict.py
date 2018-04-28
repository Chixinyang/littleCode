import sys
#通过字典推导式生成字典
mydict={x : x**2 for x in range(5) };
print(type(mydict),': ',mydict);
#遍历字典: 通过字典的items() 得到一个迭代器
for k,v in mydict.items() :
	print(k,'-',v,end="  ")
print();
#遍历序列 得到k-v对---在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
#如果不使用enumerate得到的只有序列中各个value，
mylist=list("chixinyang");
for i,v in enumerate(mylist):  
   print(i,v,end="; ")
print();
#同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#print(sys.path)
dir(sys)
