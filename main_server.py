import socket
import threading
import time
import datetime

print("Welcome to Stray Host!")

admins = ["PKB"]

print(datetime.datetime.now())

#select * from connection

with open('version', 'r') as k:
    VERSION = k.read()
    print(f"Version : {VERSION}")

HEADER = 64
FORMAT = 'utf-8'


print(" __  _____  ___    __    _    \n"
"( (`  | |  | |_)  / /\  \ \_/ \n"
"_)_)  |_|  |_| \ /_/--\  |_|  \n")

print("Starting...")


def handle_client(clientsocket, address):
    client = clientsocket.recv(1024)
    client = str(client).replace("b'", "").replace("'", "")
    try:
        with open('servers/server_list', 'r') as k:
            servers = k.read()
        if client == '0':
            print("Client detected!")
            wait_time = 0.01
            var = "b'"
            var2 = "'"
            if True:
                with open('servers/server_list', 'r') as k:
                    servers = k.read()
                    print("Sending list...")
                    clientsocket.send(servers.encode("utf-8"))
                    time.sleep(0.1)
                    server = clientsocket.recv(1024)
                    print(server)
                    server = str(server).replace("b'", "").replace("'", "")
                with open(f'servers/server_configs/{server}', 'r') as k:
                    print("start")
                    ip = k.read()
                    print(ip)
                    clientsocket.send(ip.encode("utf-8"))
                    print("sent ip")
    except:
        print("FATAL ERROR AT CLIENT HANDLING!")
    else:
        try:
            print("Server Detected!")
            with open('servers/server_list', 'a') as a:
                server_name = clientsocket.recv(1024)
                server_name = str(server_name).replace(r"\n", "")
                server_name = str(server_name).replace("b'", "").replace("'", "")
                if server_name not in servers:
                    a.write(f"{server_name}\n")
            with open(f'servers/server_configs/{server_name}', 'w') as k:
                addressdata = str(address)
                addressdata = addressdata.replace('(', '')
                addressdata = addressdata.replace(')', '')
                addressdata = addressdata.replace("'", "")
                head, sep, tail = addressdata.partition(',')
                k.write(head)
        except:
            print("FATAL ERROR AT Server Indexing!")


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(None)
    print('[STARTING] Binding sockets...')

    s.bind(('127.0.0.1', 5667))  # general interface
    s.listen(10)
    print('[STARTING] Started!')
    print('[LISTENING] Listening for maximum 10 users...')
    while True:  # might be a huge risk for the cloud
        clientsocket, address = s.accept()
        print(f'[CLIENT] Got connection : {address}')

        t = threading.Thread(target=handle_client, args=(clientsocket, address))
        t.start()


print('[STARTING] Starting...')
listen()

