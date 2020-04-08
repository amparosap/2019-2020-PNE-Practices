import socket
import termcolor
###La IP va cambiando dependiendo del terminal desde el que se ejecute
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

    def ping(self):
        print("Ok!")