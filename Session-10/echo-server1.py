import socket

ip = "192.168.1.39"
port = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((ip, port))
ls.listen()

while True:

    print("Waiting for clients to connect")

    try:
        (cs, cs_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Ser-ver stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server")
        msg_bytes = cs.recv(2840)
        msg = msg_bytes.decode()
        print(f"Received message: {msg}")
        response = "ECHO: " + msg + "\n"
        cs.send(response.encode())
        cs.close()