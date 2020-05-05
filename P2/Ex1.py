from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.39"
PORT = 8080

c = Client(IP, PORT)

c.ping()

print(f"IP: {c.ip}, {c.port}")