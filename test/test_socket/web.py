# coding:utf-8
import socket


def handle_request(client):
    buf = client.recv(1024)
    msg = "HTTP/1.1 200 OK\r\n\r\n"
    client.send(msg.encode('utf-8'))
    msg = "Hello, World"
    client.send(msg.encode('utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.3.8', 8080))
    sock.listen(5)
    a = 1
    while True:
        a += 1
        connection, address = sock.accept()
        print('访问IP:%s' % str(address))
        handle_request(connection)
        connection.close()
        print('访问量：%d' % a)


if __name__ == '__main__':
    main()
