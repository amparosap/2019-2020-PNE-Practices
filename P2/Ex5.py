from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

ip = "192.168.1.39"
port = 8080

folder = "../Session-04/"
file = "U5.txt"

c = Client(ip, port)
print(c)

seq = Seq().read_fasta(folder + file)

c.debug_talk("Sending U5 gene to the server...")
c.debug_talk(str(seq))