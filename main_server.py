import socket
import threading
import time
import datetime
import logging
from sys import stdout

logger = logging.getLogger("app")
logging.basicConfig(stream=stdout, encoding='utf-8', level=logging.DEBUG)

logger.info("Welcome to Stray Host!")

admins = ["PKB"]

logger.info(datetime.datetime.now())

with open('version', 'r') as k:
    VERSION = k.read()
    logger.info(f"Version : {VERSION}")

HEADER = 64
FORMAT = 'utf-8'


logger.info("""
 __  _____  ___    __    _    
( (`  | |  | |_)  / /\  \ \_/ 
_)_)  |_|  |_| \ /_/--\  |_|  """)

logger.info("Starting...")


def handle_client(clientsocket, address):
    client = clientsocket.recv(1024)
    client = str(client).replace("b'", "").replace("'", "")
    try:
        with open('servers/server_list', 'r') as k:
            servers = k.read()
        if client == '0':
            logger.info("Client detected!")
            wait_time = 0.01
            var = "b'"
            var2 = "'"
            with open('servers/server_list', 'r') as k:
                servers = k.read()
                logger.info("Sending list...")
                clientsocket.send(servers.encode("utf-8"))
                time.sleep(0.1)
                server = clientsocket.recv(1024)
                logger.info(server)
                server = str(server).replace("b'", "").replace("'", "")
            with open(f'servers/server_configs/{server}', 'r') as k:
                logger.info("start")
                ip = k.read()
                logger.info(ip)
                clientsocket.send(ip.encode("utf-8"))
                logger.info("sent ip")
    except Exception as e:
        logger.info("FATAL ERROR AT CLIENT HANDLING!")
        logger.info(e)
    else:
        try:
            logger.info("Server Detected!")
            with open('servers/server_list', 'a') as a:
                server_name = clientsocket.recv(1024)
                logger.info(server_name)
                server_name = str(server_name).replace(r"\n", "")
                server_name = str(server_name).replace("b'", "").replace("'", "")
                if server_name not in servers:
                    a.write(f"{server_name}\n")
            with open(f'servers/server_configs/{server_name}', 'w') as k:
                addressdata = str(address)
                logger.info(addressdata)
                addressdata = addressdata.replace('(', '')
                addressdata = addressdata.replace(')', '')
                addressdata = addressdata.replace("'", "")
                head, sep, tail = addressdata.partition(',')
                k.write(head)
        except Exception as error:
            logger.info("FATAL ERROR AT Server Indexing!")
            logger.info(f"{type(error).__name__}: {error}")


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(None)
    logger.info('[STARTING] Binding sockets...')

    s.bind(('127.0.0.1', 5667))  # general interface
    s.listen(10)
    logger.info('[STARTING] Started!')
    logger.info('[LISTENING] Listening for maximum 10 users...')
    while True:  # might be a huge risk for the cloud
        clientsocket, address = s.accept()
        logger.info(f'[CLIENT] Got connection : {address}')

        t = threading.Thread(target=handle_client, args=(clientsocket, address))
        t.start()


logger.info('[STARTING] Starting...')
listen()

