import sys,os
#print(dir(sys))
#文件操作，打开，关闭，读，写，追加
file=open("ccc.txt","w+")
fid=file.fileno()  # 得到一个文件的文件描述符
print(fid);
print(os.fstat(fid)) # 得到文件状态信息
cNum=0;
cNum=file.write("asdfasdfasdf~\n")
checknum = lambda a : a if a>0 else 0;
pos=file.tell();  #返回当前文件指针位置
cstr=file.read(); #当文件打开模式是a+的时候，文件的指针只在文档的末尾，所以读取不到任何内容
file.seek(0,0)
nstr=file.readlines();
'''while nstr:
 	print(nstr)
 	nstr = file.readline() #每次读完文件位置就会向后加1
'''
print('{name} 本次写入了{fi}字节，当前文件位置是{fpos},行读取内容是{lstr},整个文档内容是：{se}'
		.format(name=file.name,fi= checknum(cNum) ,se=cstr,fpos=pos,lstr=nstr));
#print("123456789000000000\n",repr(cstr).rjust(20,'w'))
#print("123456789000000000\n",repr(cstr).center(20,'w'))
file.close()
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:   #把异常的描述语句作为参数打印出来
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz")