import sys 
import time,functools
def mylog(func):
	def wrapper(*args, **kw):
		currenttime=time.strftime( "%x %X"  ,time.localtime())
		print('%s() time is  %s:' % (func.__name__,currenttime) )
		return func(*args, **kw)
	return wrapper
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('cxy')
def now(name):
	print('2015-3-25 : {}'.format(name))
#now=log('cxy')(now)
now('ccc')
print(now.__name__)

@mylog
def test_args(first, second, third, fourth, fifth):
	print ('First argument:  ', first )
	print ('Second argument: ', second )
	print ('Third argument:  ', third )
	print ('Fourth argument: ', fourth )
	print ('Fifth argument:  ', fifth )

# Use *args
args = [1, 2, 3, 4, 5]
test_args(*args)
print(test_args.__name__)
# Use **kwargs
kwargs = {'first' : 1,'second': 2,'third' : 3,'fourth': 4,'fifth' : 5}
#test_args(**kwargs)