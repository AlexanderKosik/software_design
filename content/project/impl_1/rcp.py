from socketserver import BaseRequestHandler, TCPServer
from jsonschema import validate
import time
import json


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            print("Message received:", msg)
            if msg:
                print("if msg was triggered")
                json_payload = json.loads(msg) # this turns a string into a python dict
                schema = json.loads(open('json/json_book.schema').read()) # dictionary
                print(validate(json_payload, schema))

            else:
                break


if __name__ == '__main__':
    print("Waiting for connection ...")
    serv = TCPServer(('', 20_001), EchoHandler)
    serv.serve_forever()
