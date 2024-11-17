import socket
import threading
import os
import logging
from sys import stdout

logging.basicConfig(stream=stdout, encoding='utf-8', level=logging.DEBUG)

class MainServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.logger = logging.getLogger("MainServer")
        #self.logger.info("""
            #__  _____  ___    __    _
            #( (`  | |  | |_)  / /\  \ \_/
            #_)_)  |_|  |_| \ /_/--\  |_|  """)

        self.logger.info(f"Starting main server on {host}:{port}")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(None)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        self.logger.info("Waiting for connections!")
        self.logger.warning("Maximum 10 concurrent users allowed!")
        while True:
            client_socket, client_address = self.socket.accept()
            self.logger.info(f"Connection from {client_address[0]} established!")
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()
        
    def handle_client(self, client_socket: socket.socket, client_address:socket.AddressInfo):
        is_server = client_socket.recv(1).decode() == "1"
        if is_server:
            servername = client_socket.recv(1024).decode().strip()
            self.logger.info(f"Got server connection from {servername}!")
            saved_servers = os.listdir("server/servers/server_configs")
            if servername not in saved_servers:
                with open("server/servers/server_configs/" + servername, "w") as serverfile:
                    serverfile.write(str(client_address[0]))
        else:
            # send back list of available servers
            servers = os.listdir("server/servers/server_configs")
            serverlist_message = "\n".join(servers)
            client_socket.send(serverlist_message.encode())
            # receive server selection
            selected_server = client_socket.recv(1024).decode()
            # connect to selected server
            with open(f"server/servers/server_configs/{selected_server}", "r") as server_config:
                server_address = server_config.read()
                client_socket.send(server_address.encode())
            # My work here is done
            client_socket.close()

if __name__ == "__main__":
    main_server = MainServer("127.0.0.1", 6081)
    main_server.start()
