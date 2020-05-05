import socket

ip = "192.168.1.39"
port = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((ip, port))

ls.listen()

print("Server configured")

connections = 0
client_list = []
okay = True

while okay:

    print("Wainting for a client to connect")

    try:
        (cs, cs_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by user")

        ls.close()
        exit()

    else:

        print("A client has connected to the server")
        connections += 1

        if connections == 5:
            okay = False

        print(f"Connection {connections}. Client: IP, PORT: {cs_ip_port}")
        client_list.append(cs_ip_port)

        msg = cs.recv(2840).decode()

        print(f"Message received: {msg}")

        response = "ECHO: " + msg + "\n"

        cs.send(response.encode())

        cs.close()

print()
print("The following clients have connceted to the server: ")

for i, c in enumerate(client_list):
    print(f"Client {i}: {c}")

ls.close()