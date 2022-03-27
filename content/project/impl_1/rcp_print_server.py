from socketserver import BaseRequestHandler, TCPServer
from jsonschema import validate
import time
import json

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if msg:
                #print(msg)
                # now validate the message
                json_payload = json.loads(msg)
                schema = json.loads(open('json/json_book.schema').read())
                validate(json_payload, schema)
            else:
                break

if __name__ == '__main__':
    print("Waiting for connection ...")
    serv = TCPServer(('', 20_001), EchoHandler)
    serv.serve_forever()
