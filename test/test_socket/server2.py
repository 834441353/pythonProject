# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting...')
    conn, addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data.decode('utf-8'))
    data = '不要回答,不要回答,不要回答'
    conn.sendall(data.encode('utf-8'))

    conn.close()