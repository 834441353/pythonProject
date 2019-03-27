import sys
import socket

# 创建scoket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超时后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("链接地址：%s" % str(addr))

    msg = '啦啦啦' + "\r\n"

    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
