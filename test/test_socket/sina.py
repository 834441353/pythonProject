import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.cn', 80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# data = ''
# while True:
#     a = s.recv(60)
#     print(a)
#     if a == "b''":
#         break

    # data += str(a)

data = s.recv(1024)
print(data)
#
# data = s.recv(60)
# print(data)
#
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
s.close()
