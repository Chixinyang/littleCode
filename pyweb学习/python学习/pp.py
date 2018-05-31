#-*- coding:utf-8 -*-
import sys
def GetYangChengCash(name) :
	num=5
	if name=="胡帅":
		num +=2
		name=name+"(大老板)"
	print( '全世界就那么27个养成币，但是他--{0:10}'.ljust(15).format(name),'一个人就有{}个'.ljust(20).format(num))
namelist=('凯南','范浩然','李希','池鑫洋','胡帅')
for name in namelist :
	GetYangChengCash(name)