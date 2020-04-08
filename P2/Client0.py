import socket
import termcolor
###La IP va cambiando dependiendo del terminal desde el que se ejecute
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

    def ping(self):
        print("Ok!")

    def __str__(self):
        return (f"Connection to SERVER at {self.ip}, PORT: {self.port}")
