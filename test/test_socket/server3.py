# -*- coding:utf-8 -*-
import socket
# import sys
# import select

ip_port = ('127.0.0.1', 8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    conn, address = sk.accept()
    msg = '欢迎致电 10086，请输入1xxx,0转人工服务.'
    conn.sendall(msg.encode('utf-8'))
    Flag = True
    while Flag:
        data = conn.recv(1024).decode('utf-8')
        if data == 'exit':
            Flag = False
        elif data == '0':
            msg = '通过可能会被录音.balabala一大推'
            conn.sendall(msg.encode('utf-8'))
        else:
            msg = '请重新输入.'
            conn.sendall(msg.encode('utf-8'))
    conn.close()
