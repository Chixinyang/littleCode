import socket
#定义Ipv的流套接字
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#绑定ip地址和端口号
c.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(c.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    c.send(data)
    print(c.recv(1024).decode('utf-8'))
c.send(b'exit')
c.close()