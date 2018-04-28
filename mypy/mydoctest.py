import sys
from myclass import people
def mytest():
	'''
	test class people 
	Example:
	>>> p1=people("LiLi",18,"girl")
	>>> p1.info()
	this is 张飞,a 19-year-old man
	>>> print(p1)
	this is a LiLi,a 18-year-old girl 
	'''
def multiply(a,b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a*b
if __name__ == '__main__':
	print("start :")
	import doctest
	doctest.testmod(verbose= False)