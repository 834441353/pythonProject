# -*- coding:utf-8 -*-
import socket

ip_port = ('127.0.0.1', 8002)
sk = socket.socket()
sk.connect(ip_port)

while True:
    inp = input('please input:')
    sk.sendall(inp.encode('utf-8'))
sk.close()

