import socket
import threading
import os
import logging
import json
from sys import stdout
from time import sleep

logging.basicConfig(stream=stdout, encoding='utf-8', level=logging.DEBUG)

class ContentServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.logger = logging.getLogger("ContentServer")
        self.logger.info(f"Starting content server on {host}:{port}")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(None)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        with open("settings.json") as setting:
            self.settings = json.load(setting)
        self.logger.info("Settings loaded successfully!")
        with open("whitelist.encrypted") as whl:
            self.whitelist = whl.read().splitlines()
        self.logger.info("Whitelist loaded successfully!")
        with open("admins.json") as admin_json:
            self.admins = json.load(admin_json)
        self.logger.info("Admins loaded successfully!")
        self.clients = {}
        self.packet_delay = 0.01
    
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        self.logger.info("Waiting for connections!")
        self.logger.warning("Maximum 10 concurrent users allowed!")
        while True:
            client_socket, client_address = self.socket.accept()
            self.logger.info(f"Connection from {client_address[0]} established!")
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def handle_client(self, client_socket: socket.socket, client_address: socket.socket):
        # Send config to client
        self.logger.info("Sending settings...")

        # TODO replace waits with separator. BREEDING GROUND FOR RACE CONDITION
        client_socket.send(self.settings["names"]["label"].encode('utf-8'))
        sleep(self.packet_delay)
        client_socket.send(self.settings["names"]["server_name"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["names"]["server_name_to_show"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["buttonframe_background"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["opacity"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["label_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["label_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["label_size"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["background"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["font_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["font_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["result_text_box_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["result_text_box_edge_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["result_text_box_edge_color_selected"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["result_text_box_edge_size"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["searchbar_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["searchbar_edge_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["searchbar_edge_color_selected"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["searchbar_edge_size"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["send_command_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["send_command_text_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["send_command_pressed_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["send_command_pressed_text_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["refresh_list_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["refresh_list_text_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["refresh_list_pressed_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["refresh_list_pressed_text_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["create_new_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["create_new_text_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["create_new_pressed_background_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["colors"]["create_new_pressed_text_color"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["start_text"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["not_found"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["got_admin"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["maintenance"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["not_on_whitelist"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["help"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["added_someone_to_admins"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["failed_to_add_someone_to_admins"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["added_someone_to_whitelist"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["failed_to_add_someone_to_whitelist"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["messages"]["command_disabled"].encode("utf-8"))
        sleep(self.packet_delay)
        client_socket.send(self.settings["rules"]["rules"].encode("utf-8"))

        with open("version") as version_file:
            version = version_file.read()
            client_socket.send(version.encode("utf-8"))
            self.logger.info(f"Sent version {version} to {client_address}")

        self.logger.info("Done!")

        self.clients[client_socket] = {
            "nickname": None,
            "admin": False,
            "whitelisted": False,
            "socket": client_socket,
        }

        # Transition to command processing
        command_handlers = {
            "usr": self.user_join,
            "need": self.serve_site,
            "create": self.create_site,
            "list": self.list_sites,
            "###close": self.disconnect_user,
            "addAdmin": self.attempt_promotion,
            "whitelist": self.attempt_whitelist_addition
        }

        while True:
            if client_socket not in self.clients.keys():
                # user had disconnected
                return
            sleep(0.01)
            message = client_socket.recv(1024).decode()
            for command in command_handlers.keys():
                if message.startswith(command):
                    command_handlers[command](message, client_socket)
                    break
    
    def user_join(self, message: str, client: socket.socket):
        nickname = message[len("usr"):]
        self.clients[client]["nickname"] = nickname
        if nickname in self.admins:
            self.clients[client]["admin"] = True
            client.send(b'1')
        else:
            client.send(b"0")
        sleep(self.packet_delay)
        if nickname in self.whitelist or self.whitelist == ["open"]:
            self.clients[client]["whitelisted"] = True
        else:
            client.send(b"cl")
            # Not whitelisted -> disconnect
            self.disconnect_user(message, client)
            return
        client.send(b"let")
        self.logger.info(f"{nickname} joined!")
    
    def serve_site(self, message: str, client: socket.socket):
        site_name = message[len("need"):]
        sites = os.listdir("sites")
        sites.remove("websites.list") # we don't need to include the list file
        if site_name in sites:
            with open(f"sites/{site_name}") as site:
                client.send(site.encode())
        else:
            client.send(self.settings["messages"]["not_found"].encode())
        self.logger.info(f"{self.clients[client]['nickname']} requested {site_name}!")
    
    def create_site(self, message: str, client: socket.socket):
        site_name = message[len("create"):]
        site_file = open(f"sites/{site_name}", "w")
        need_more_content = True
        while need_more_content:
            content = client.recv(1024).decode()
            if content == "###close":
                need_more_content = False
                site_file.write(f"Created by: {self.clients[client]['nickname']}")
                self.logger.info(f"{self.clients[client]['nickname']} created {site_name}!")
                site_file.close()
            else:
                site_file.write(content + "\n")
    
    def list_sites(self, message: str, client: socket.socket):
        sites = os.listdir("sites")
        sites.remove("websites.list") # we don't need to include the list file
        client.send("\n ".join(sites).encode())
    
    def disconnect_user(self, message: str, client: socket.socket):
        self.logger.info(f"{self.clients[client]['nickname']} has left.")
        del self.clients[client]
        client.close()
    
    def attempt_promotion(self, message: str, client: socket.socket):
        username = client.recv(1024).decode()
        if self.clients[client]["admin"]:
            if username in self.admins:
                self.logger.info(f"{username} is already an admin.")
                client.send(self.settings["messages"]["failed_to_add_someone_to_admins"].encode())
            else:
                self.admins.add(username)
                self.logger.info(f"{self.clients[client]['nickname']} promoted {username} to admin.")
                client.send(self.settings["messages"]["added_someone_to_admins"].format(username).encode())
        else:
            client.send(self.settings["messages"]["command_disabled"].encode())
    
    def attempt_whitelist_addition(self, message: str, client: socket.socket):
        username = client.recv(1024).decode()
        if self.clients[client]["admin"]:
            if username in self.whitelist:
                self.logger.info(f"{username} is already whitelisted.")
                client.send(self.settings["messages"]["failed_to_add_someone_to_whitelist"].encode())
            else:
                self.whitelist.add(username)
                self.logger.info(f"{self.clients[client]['nickname']} whitelisted {username}.")
                client.send(self.settings["messages"]["added_someone_to_whitelist"].format(username).encode())
        else:
            client.send(self.settings["messages"]["command_disabled"].encode())
    
if __name__ == "__main__":
    server = ContentServer("127.0.0.1", 5666)
    server.start()