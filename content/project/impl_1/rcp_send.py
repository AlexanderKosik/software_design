import argparse
import time
from socket import socket, AF_INET, SOCK_STREAM
from os import listdir
from os.path import isfile, join

# arg parsing
# destination
# port
# json directory


ip = "127.0.0.1"
port = 20_001
json_dir = 'json/'
BLOCK_SIZE = 1024

def connect():
    """
    Tries to connect to ip and port every 2 seconds
    """
    s = socket(AF_INET, SOCK_STREAM)
    print(f"[TRY]\tConnecting to {ip}:{port} ", end="")
    while s.connect_ex((ip, port)) != 0:
        print(".", end="", flush=True)
        time.sleep(2.0)
    print("\n[OK]\tConnection established")
    return s

def read_json_files():
    """
    Returns all json files in json_dir
    """
    return [
        (f, join(json_dir, f)) 
        for f in listdir(json_dir) 
        if isfile(join(json_dir, f)) and f.endswith('.json')
    ]


def print_menu():
    """
    Prints a file menu for selection
    """
    files = read_json_files()
    print("--- Select file for transmission | Ctrl+C to terminate ---")
    for file_no, (file, path) in enumerate(files):
        print(f"[{file_no}]: {file}")

sock = connect()

while True:
    print_menu()
    selection = int(input("File number: "))
    files = read_json_files()
    if  0 <= selection < len(files):
        fn, fqfn = files[selection]
        print(f"[TRY]\tTransmitting file {fn}")
        with open(fqfn, 'rb') as f:
            transmitted = 0
            while content := f.read(BLOCK_SIZE):
                sock.send(content)
                transmitted += len(content)
            print(f"[OK]\tTransmission done ({transmitted} bytes transmitted)")
    else:
        print("Invalid file selection")
