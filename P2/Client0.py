import socket
import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK")

    def __str__(self):
        return f"Connection at IP: {self.ip}, PORT: {self.port}"

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port)) # Establish connection
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8") # Receive message
        s.close()
        return response # The output is the message received from the server

    def debug_talk(self, msg_to_server):
        msg_from_server = self.talk(msg_to_server)
        print("To server: ", end = '')
        termcolor.cprint(msg_to_server, "blue")
        print("From server: ", end = '')
        termcolor.cprint(msg_from_server, "green")