from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

ip = "192.168.1.39"
port = 8080

c = Client(ip, port)
print(c)

folder = "../Session-04/"
file = "U5.txt"

seq = Seq().read_fasta(folder + file)

print(f"Gene FRAT1: {str(seq)}")

length = 10

c.talk(f"Sending FRAT1 gene to the server in fragments of {length} bases...")

for i in range(5):
    frag = str(seq)[i * length: (i + 1) * length] #para q empiece desde el 1, 11,21....
    print(f"Fragment {i+1}: {frag}")
    c.talk(f"Fragment {i+1}: {frag}")