import sys
#print(sys.path)
def func(n):
	a,b ,counter= 1,0,0;
	while counter < n :
		a,b=b,a+b; #<=>tuple(b,a+b)
		print(b,end=", ");
		counter += 1;
		pass
#func(10);
"""学习 生成器 --构建方式，访问方式
	使用yeild（捕获）的函数被称为生成器，返回一个迭代器，该迭代器访问只能通过循环遍历或者next()访问
	函数执行到yeild语句时，会保存当前函数的执行状态（当该状态被调用后会返回b的值），
	然后继续执行下一个，或者抛出StopIteration异常。
"""
def generator_func(n):
	a,b,cunt=1,0,0;
	while cunt < n :
		a,b=b,a+b;
		yield b;
		cunt +=1;
		pass
generator=generator_func(10);
while True:
	try:
		print(next(generator) ,end=", ");
	except StopIteration :
		#sys.exit();  #会直接结束程序运行
		break;  	  #跳出循环
	pass
print();
"""获得生成器的另一种方式"""
generator2=(x**2 for x in range(10) );
for item in generator2:
	print(item,end=", ");
print();
"""迭代器"""
str='cxy is a student';
info=list(str);
print( type(info),' :',info );
it=iter(info);   #转换成迭代器
for item in it : 
	print(item,end='');
print();
"""lambda表达式： 表达式的类型是函数"""
li = [11, 22, 33]
new_list = lambda : 2 + 10
print(type(new_list))
print(new_list())
"""矩阵   转置"""
matrix=[         #定义一个3*4的矩阵--实际上是一个list，不过list的内部元素也是list
	[0,1,2,3],
	[4,5,6,7],
	[8,9,10,11],
] 
print(type(matrix)," :",matrix); 
matrix_re=[ row[i] for i in range(4) for row in matrix ];  #循环嵌套
print(matrix_re);
matrix_re=[ row[i] for row in matrix for i in range(4) ]; #从左到右，左边的for在最外层
"""
	列表推导式需要把右边表达式的结果返回给左边
	for row in matrix for i in range(4) 是一个for的嵌套，作为一个整体，返回结果给row【i】
"""
print(matrix_re);
matrix_re=[ [row[i] for row in matrix] for i in range(4) ]; #加了【】 表明for的结果是一个list，右边的for在最外层
"""[row[i] for row in matrix] 需要右边表达式结果作为输入，然后运算得到一个list"""
print(matrix_re);
for i in range(4) :
	for n in range(3):
		matrix_re[i][n]=matrix[n][i];
	pass
pass
print(matrix_re)
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed);
"""定义字典"""
dic1=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dic2=dict(sape=4139, guido=4127, jack=4098)