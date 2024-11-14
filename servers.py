import threading, logging
from time import sleep

from main_server_refactored import MainServer
from content_server_refactored import ContentServer

logging.basicConfig(level=logging.DEBUG)

class ArcticServer:
    def __init__(self):
        self.main_server = MainServer("127.0.0.1", 5667)
        self.content_server = ContentServer("127.0.0.1", 5666)
        self.logger = logging.getLogger("ArcticServer")
        self.logger.info("Starting Arctic Server...")
        self.main_server_thread = threading.Thread(target=self.main_server.start)
        self.content_server_thread = threading.Thread(target=self.content_server.start)
    
    def start(self):
        self.main_server_thread.start()
        self.content_server_thread.start()
        self.logger.info("Servers started!")

if __name__ == "__main__":
    server = ArcticServer()
    server.start()