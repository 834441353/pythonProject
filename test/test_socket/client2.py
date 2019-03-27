# -*- coding:utf-8 -*-
import socket

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)
data = '请求占领地球'
sk.sendall(data.encode('utf-8'))

server_reply = sk.recv(1024)
print(server_reply.decode('utf-8'))

sk.close()