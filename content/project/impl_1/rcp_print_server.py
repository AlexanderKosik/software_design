from socketserver import BaseRequestHandler, TCPServer
import time

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if msg:
                print(msg)
            else:
                break

if __name__ == '__main__':
    serv = TCPServer(('', 20_001), EchoHandler)
    serv.serve_forever()
