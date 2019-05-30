import socketserver
import os
import json


class EchoHandler(socketserver.BaseRequestHandler, socketserver.BaseServer):
    def handle(self):
        print('Connected from: ', self.client_address)
        while True:
            recvData = self.request.recv(1024)
            # print(recvData)
            # self.request.sendall(recvData)
            if not recvData:
                break
            a = 'hello'
            self.request.sendall(a.encode('utf-8'))
        self.request.close()

        print("Disconnected from :", self.client_address)


srv = socketserver.ThreadingTCPServer(('', 4424), EchoHandler)
srv.serve_forever()
