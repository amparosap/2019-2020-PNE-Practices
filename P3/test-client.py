from Client0 import Client

print("-----| Practice 3, Exercise 7 |------")

ip = "192.168.1.39"
port = 8080

c = Client(ip, port)
print(c)

command0 = "GET 0"
gene0 = c.talk(command0)

print("Testing PING...")
print(c.talk("PING"))

print()
print("Testing GET...")

for i in range(5):
    command = f"GET {i}"
    print(f"{command}: {c.talk(command)}")

print()
print("Testing INFO...")
print(c.talk("INFO" + gene0))

print()
print("Testing COMP...")
print(c.talk("CONP" + gene0))

print()
print("Testing REV...")
print(c.talk("REV" + gene0))

print()
print("Testing GENE...")

for gene in ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]:
    print("Gene: ", gene)
    print(c.talk(f"GENE {gene}"))