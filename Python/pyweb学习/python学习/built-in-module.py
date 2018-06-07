import sys
#test collections module
def test_nametuple():
	''' test namedtuple 自定义tuple
	>>> from collections import namedtuple
	>>> Point = namedtuple('Point', ['x', 'y'])
	>>> p = Point(1, 2)
	>>> p.x
	1
	>>> p.y
	2
	>>> isinstance(p, Point)
	True
	>>> isinstance(p, tuple)
	True
	'''
def test_deque ():
	'''test deque 队列--可快速增删的双向队列
	>>> from collections import deque
	>>> q = deque(['a', 'b', 'c'])
	>>> q.append('x')
	>>> q.appendleft('y')
	>>> q
	deque(['y', 'a', 'b', 'c', 'x'])
	'''
import base64

def safe_base64_decode(s):
    num = 4 - len(s)%4  #计算 差多少位能达到4的倍数
    while num:
        s = s + bytes('=','utf-8') #每差一位就往后面加上一个=的比特数
        num = num - 1
    return base64.b64decode(s)

# 测试:
'''
 	如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
 Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
 	由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'
去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
'''
print("b'abcd' == ",safe_base64_decode(b'YWJjZA=='))
print("b'abcd' == ",safe_base64_decode(b'YWJjZA'))
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
#测试  摘要算法和hmac算法
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])  #给每一个用户一个自己的key
        print("key = ",self.key)
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),  #只有在查询的时候在构建对象
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)
if __name__ == '__main__':
	print("start :")
	print(login("michael",'123456'))
	import doctest
	#doctest.testmod(verbose= True)