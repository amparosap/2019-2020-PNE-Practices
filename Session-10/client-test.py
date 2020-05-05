from Client0 import Client

# -- Parameters of the server to talk to
PORT = 8080
IP = "192.168.1.39"

# -- Repeat five times
for i in range(5):
    c = Client(IP, PORT)
    c.debug_talk(f"Message {i}")