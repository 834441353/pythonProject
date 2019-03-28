# -*- coding:utf-8 -*-
import sys
import select
import socket

sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk1.bind(('127.0.0.1', 8002))
sk1.listen(5)
sk1.setblocking(0)

inputs = [sk1, ]
while True:
    realable_list, writeable_list, error_list = select.select(inputs, [], inputs, 1)
    for r in realable_list:
        # 当客户端第一次连接服务端时
        if sk1 == r:
            print('accept')
            request, address = r.accept()
            request.setblocking(0)
            inputs.append(request)
        # 当客户端连接上服务端之后，再次发送数据时
        else:
            received = r.recv(1024)
            # 当正常接收客户点发送的数据时
            if received:
                print('received data:', received.decode('utf-8'))
            # 当客户端关闭时
            else:
                inputs.remove(r)

sk1.close()
