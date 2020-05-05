from Client0 import Client

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

ip = "192.168.1.39"
port = 8080

c = Client(ip, port)

c.debug_talk("Message 1: ---")
c.debug_talk("Message 2: Testing")