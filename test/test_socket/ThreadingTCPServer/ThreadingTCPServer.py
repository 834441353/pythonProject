# -*- coding:utf-8 -*-
import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        msg = '0转人工'
        conn.sendall(msg.encode('utf-8'))
        Flag = True
        while Flag:
            data = conn.recv(1024).decode('utf-8')
            if data == 'exit':
                Flag = False
            elif data == '0':
                msg = 'balabala一大堆'
                conn.sendall(msg.encode('utf-8'))
            else:
                msg = '请从新输入'
                conn.sendall(msg.encode('utf-8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8090), MyServer)
    server.serve_forever()
