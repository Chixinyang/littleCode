import socket,threading,time
#服务端处理函数
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')#发送欢迎信息
    while True:
        data = sock.recv(1024)#等待客户端返回响应
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
#定义Ipv的流套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#绑定ip地址和端口号
s.bind ( ('127.0.0.1',9999)  )
#监听--限制链接个数
s.listen(5)
print('waitting for connection......')
while True:
    #接受链接,返回一个二元的tuple
    sock,addr=s.accept()
    #创建线程进行处理
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

